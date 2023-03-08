# Grafana K6

## 참조

- [grafana/k6](https://github.com/grafana/k6)

## 실행

```sh
sudo docker compose up -d influxdb grafana
```

```sh
# sudo docker compose up k6
sudo docker compose run -v $PWD/samples:/scripts k6 run /scripts/stages.js
```

### Grafana 재시작할 때

```sh
sudo docker compose stop grafana
sudo docker compose rm grafana
```

```sh
sudo docker compose up -d grafana
```

## Data sources

> Configuration > Data sources > influxdb > database: k6 지정

database 설정이 계속 누락됨

## Dashboards

- 4411: [K6 - HTTP Requests](https://grafana.com/grafana/dashboards/4411)
