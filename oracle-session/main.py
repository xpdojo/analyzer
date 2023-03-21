import os
import time
from datetime import datetime, timezone, timedelta
from typing import Collection, Generator, Any

import oracledb
from elasticsearch.client import Elasticsearch

from sql import oracle_session

KST = timezone(timedelta(hours=9))


def lower_dict_keys(d) -> dict:
    return {k.lower(): v for k, v in d.items()}


def fetch(
        iterable: Collection,
        batch_size: int = 1_000,
) -> Generator[Any, Any, None]:
    """
    [
        {'index': {'_index': 'oracle-session-2023.03.18', '_id': 2947}},
        {'sid': 2947, 'serial#': 24937, 'wait_time': -1, 'seconds_in_wait': 0, 'state': 'WAITED SHORT TIME','event': 'PGA memory operation', ...}
    ]
    """
    batch_size *= 2  # (index, doc) 벌크 인덱스 시 2줄을 함께 처리
    length = len(iterable)
    for i in range(0, length, batch_size):  # 0~len(iterable) 범위를 batch_size만큼씩 반복
        yield iterable[i:min(i + batch_size, length)]  # [0:1000] -> 0~999, [1000:2000] -> 1000~1999, ...


def with_timezone(date_str: datetime) -> datetime | None:
    if date_str is None:
        return None
    return date_str.astimezone(KST)


def main(
        index_name: str,
        batch_size: int,
):
    # Oracle 접속
    connection = oracledb.connect(
        user=os.getenv('ORACLE_DB_USER', default='sysadmin'),
        password=os.getenv('ORACLE_DB_PASSWORD', default='sysadmin'),
        dsn=os.getenv('ORACLE_DB_DSN', default='localhost:1521/orcl')
    )

    query = oracle_session.query()

    oracle_result = []
    with connection.cursor() as cursor:
        cursor.execute(statement=query)
        columns = [col[0] for col in cursor.description]
        cursor.rowfactory = lambda *args: dict(zip(columns, args))
        for row in cursor:
            oracle_result.append(row)

    # Elastic Cloud 접속
    es = Elasticsearch(
        cloud_id=os.getenv(key='ELASTIC_CLOUD_ID'),
        http_auth=(
            os.getenv(key='ELASTIC_USERNAME', default='elastic'),
            os.getenv(key='ELASTIC_PASSWORD', default=''),
        )
    )
    # print(es.info())

    timestamp = '@timestamp'
    sql_exec_start = 'sql_exec_start'
    sql_fulltext = 'sql_fulltext'
    prev_sql_fulltext = 'prev_sql_fulltext'

    # Transform
    docs = []
    for src in oracle_result:
        # mutate
        source = lower_dict_keys(src)

        # date format
        source[sql_exec_start] = with_timezone(source[sql_exec_start])
        source[timestamp] = datetime.now(tz=KST)

        # print(type(lower_src[sql_fulltext])) # <class 'oracledb.LOB'>
        if source[sql_fulltext] is not None:
            source[sql_fulltext] = ''.join(source[sql_fulltext].read())
        if source[prev_sql_fulltext] is not None:
            source[prev_sql_fulltext] = ''.join(source[prev_sql_fulltext].read())

        for remove_field in [
            # sql_fulltext,
            # prev_sql_fulltext,
        ]:
            if remove_field in source:
                del source[remove_field]

        # identifier
        # https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SESSION.html
        # https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SQL_MONITOR.html
        prev_exec_start: datetime = source['prev_exec_start']
        prev_exec_start_epoch: float = datetime.timestamp(prev_exec_start)
        _id = f"{source['prev_exec_id']}-{source['prev_sql_id']}-{int(prev_exec_start_epoch)}"

        docs.append({"index": {"_index": index_name, "_id": _id}})
        docs.append(source)

    # Bulk Index
    for result in fetch(docs, batch_size):
        bulk = es.bulk(index=index_name, body=result)
        print(f"batch_docs {len(bulk['items'])}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="""
    Oracle DB Session 정보를 Elastic Cloud에 저장합니다.
    """)
    parser.add_argument('-n', '--interval', metavar='seconds', required=False,
                        default=5, type=int,
                        help='Specify  update  interval. (default: 5 seconds)')
    parser.add_argument('-i', '--index-name', metavar='name', required=False,
                        default='oracle-session-2023.03.21v2', type=str,
                        help='Elasticsearch index name.')

    args = parser.parse_args()

    while True:
        main(
            index_name=args.index_name,
            batch_size=1_000,
         )
        time.sleep(args.interval)
