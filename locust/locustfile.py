from locust import HttpUser, task, between


class Load(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/api/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })

    @task
    def simple_request(self):
        self.client.get("/errors")
        self.client.get("/api/users/2")

    @task(3)
    def list_users(self):
        for item_id in range(2):
            self.client.get(f"/api/users?page={item_id}", name="List Users")
