# Prometheus with Grafana

- 시스템 메트릭 O
- APM, 로그 추적 X

Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud.
Since its inception in 2012, many companies and organizations have adopted Prometheus,
and the project has a very active developer and user community.
It is now a standalone open source project and maintained independently of any company.

## Using docker compose

```sh
sudo docker compose up -d
```

## Exporters

- Node Exporter
- SNMP Exporter
- Blackbox Exporter

## Grafana Dashboard

- [Dashboard Hub](https://grafana.com/grafana/dashboards/)
  - 1860:[Node Exporter Full](https://grafana.com/grafana/dashboards/1860-node-exporter-full/)

## 참조

- [PagerTree/prometheus-grafana-alertmanager-example](https://github.com/PagerTree/prometheus-grafana-alertmanager-example)
- [Grafana dashboards](https://grafana.com/grafana/dashboards/)
