from locust import HttpUser, task, between


# https://docs.locust.io/en/stable/writing-a-locustfile.html
# https://github.com/locustio/locust/blob/master/examples
class Load(HttpUser):
    """
    python -m locust -f locustfile.py --headless --host=https://reqres.in -u 10 -r 2 -t 1m --csv=results
    """

    # 각 사용자가 작업을 완료한 후 1~3초 사이의 랜덤한 시간 동안 대기합니다. 
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.post("/api/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        # print(response.json())
        self.token = response.json()['token']
        self.client.headers = {**self.auth_headers(), **self.client.headers}

    def auth_headers(self):
        return {"Authorization": "Bearer " + self.token}

    @task
    def simple_request(self):
        self.client.get("/errors")
        self.client.get("/api/users/2")

    @task(3)
    def list_users(self):
        for item_id in range(2):
            self.client.get(f"/api/users?page={item_id}", name="List Users")
