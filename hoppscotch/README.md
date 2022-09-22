# Hoppscotch

원래 프로젝트명이 Postwoman일 정도로 Postman과 굉장히 유사한 웹 API 애플리케이션이다.
Postman에 비해 불편한 점들이 있지만 오픈 소스이기 때문에 무료로 사용할 수 있다.

## 개발 환경에서 실행하기

### hoppscotch

```sh
docker compose up -d
```

### proxyscotch

```sh
curl -L https://github.com/hoppscotch/proxyscotch/releases/download/v0.1.1/proxyscotch-server-linux-amd64-v0.1.1 -o proxyscotch
```

```sh
chmod +x ./proxyscotch
```

```sh
./proxyscotch
```

> Settings > Use the proxy middleware to send requests > http://localhost:9159

## 참조

- [hoppscotch/hoppscotch](https://hub.docker.com/r/hoppscotch/hoppscotch) - Docker Hub
