from locust import HttpUser, task, between


# https://docs.locust.io/en/stable/writing-a-locustfile.html
# https://github.com/locustio/locust/blob/master/examples
class Load(HttpUser):
    """
    python -m locust -f locustfile-get.py --headless --host=https://reqres.in -u 10 -r 2 -t 1m --csv=results
    """

    # 각 사용자가 작업을 완료한 후 1~3초 사이의 랜덤한 시간 동안 대기합니다.
    # wait_time = between(1, 3)

    @task(weight=10)
    def simple_request(self):
        self.client.get("/api/country?lang=en")

