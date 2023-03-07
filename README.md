# 분석

## Load Test

- [Apache JMeter](https://github.com/apache/jmeter)
- [Locust](https://locust.io/): Python 스크립트
- [NGrinder](https://github.com/naver/ngrinder): Groovy 스크립트
- [Gatling](https://gatling.io/): Scala 스크립트

## API platform

- [Hoppscotch (Postwoman)](https://hoppscotch.io/)
- [Postman](https://www.postman.com/): 프리 티어 있음

## Visualize

대부분 time-series 데이터를 시각화하는데 사용한다.

- [Grafana](https://grafana.com/)
- [Kibana](https://www.elastic.co/kibana/)
- [Graphite](https://graphiteapp.org/)

## Trace

> [Dapper: a Large-Scale Distributed Systems Tracing Infrastructure](https://research.google/pubs/pub36356/) - Google

- [Jaeger](https://www.jaegertracing.io/)
  - [OpenTracing](https://opentracing.io/docs/getting-started/)
- [Zipkin](https://zipkin.io/pages/quickstart)
- [OpenTelemetry](https://opentelemetry.io/)

## Log Collector

- [Loki](https://github.com/grafana/loki)
- [Fluentd](https://docs.fluentd.org/)
- [Logstash](https://www.elastic.co/logstash/)

## Metric Collector

- [Prometheus](https://prometheus.io/)
- [Metricbeat](https://www.elastic.co/beats/metricbeat)

## APM

- [Elastic APM](https://github.com/elastic/apm)
- [Apache SkyWalking](https://skywalking.apache.org/)
- [Pinpoint](https://github.com/pinpoint-apm/pinpoint-docker)
- [SigNoz](https://github.com/SigNoz/signoz)
- [Datadog](https://www.datadoghq.com/): 유료
- [Sentry](https://sentry.io/): 유료
- [WhaTap](https://www.whatap.io/): 유료

## JVM

- [Eclipse Memory Analyzer (MAT)](https://www.eclipse.org/mat/): 힙 덤프 분석
- [VisualVM](https://visualvm.github.io/download.html): 실시간 애플리케이션 분석
  - VisualGC: GC 관련 메트릭 시각화
