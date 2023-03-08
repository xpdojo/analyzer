# Locust

## 스크립트 편집

- [Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) - locust.io

```sh
python3 -m venv venv
source venv/bin/activate
```

```sh
pip install locust
```

- [Command Line Options](https://docs.locust.io/en/stable/configuration.html#command-line-options) - locust.io

```sh
python -m locust -f locustfile.py --headless --host=https://reqres.in -u 10 -r 2 -t 1m --csv=results
```

```sh
source venv/bin/deactivate
```

## Docker compose를 사용해서 실행

```sh
sudo docker compose up --scale worker=4
```
