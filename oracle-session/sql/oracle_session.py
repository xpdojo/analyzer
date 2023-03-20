def query():
    """
    [Oracle Database Release 19 V$SESSION](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-SESSION.html)
    [WAIT_TIME_MICRO, TIME_SINCE_LAST_WAIT_MICRO](https://m.blog.naver.com/hanajava/221017416454)
    """
    return """
SELECT *
FROM (SELECT sess.sid,
             sess.serial#,
             ROUND(sess.wait_time_micro / 1000, 2)            wait_time_millis,
             ROUND(sess.time_since_last_wait_micro / 1000, 2) time_since_last_wait_millis,
             CASE
                 WHEN sess.status = 'ACTIVE'
                     THEN sess.last_call_et
                 ELSE 0
                 END                                          active_elapsed_time_secs,
             sess.state,
             sess.event,
             sess.username,
             sess.osuser,
             sess.machine,
             sess.program,
             sess.type,
             sess.sql_child_number,
             sess.sql_exec_start,
             sess.sql_id,
             (SELECT sql.sql_fulltext
              FROM v$sql sql
              WHERE sess.sql_id = sql.sql_id
                  FETCH FIRST 1 ROWS ONLY) sql_fulltext,
             sess.prev_exec_start,
             sess.prev_sql_id,
             (SELECT sql.sql_fulltext
              FROM v$sql sql
              WHERE sess.prev_sql_id = sql.sql_id
                  FETCH FIRST 1 ROWS ONLY) prev_sql_fulltext,
             blocking_session
      FROM v$session sess
      WHERE sess.username != 'SYS'
      ORDER BY logon_time DESC)
WHERE dbms_lob.compare(prev_sql_fulltext,
                       'update user$ set spare6=DECODE(to_char(:2, ''YYYY-MM-DD''), ''0000-00-00'', to_date(NULL), :2) where user#=:1') != 0
"""
