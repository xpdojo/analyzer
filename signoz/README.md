# SigNoz

- 오픈 소스
- 메트릭, Tracing 등 종합 APM
- 컬럼 기반(columnar) OLAP datastore인 [ClickHouse](https://github.com/ClickHouse/ClickHouse)에 데이터 저장
- 화면은 리액트

## Using Docker Compose

- [Docs](https://signoz.io/docs/install/docker/#install-signoz-using-docker-compose)

```sh
git clone --depth=1 -b main https://github.com/SigNoz/signoz.git && cd signoz/deploy/
```

```sh
sudo docker compose -f docker/clickhouse-setup/docker-compose.yaml up -d
```

[frontend(localhost:3301)](http://localhost:3301/) 접속
