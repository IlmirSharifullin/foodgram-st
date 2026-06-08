from locust import HttpUser, between, task


DEFAULT_HEADERS = {"Host": "foodgram.localhost.ru"}


class FoodgramReadOnlyUser(HttpUser):
    wait_time = between(0.5, 2.0)

    @task(5)
    def recipes(self):
        self.client.get(
            "/api/recipes/?page=1&limit=6",
            headers=DEFAULT_HEADERS,
            name="/api/recipes/",
            timeout=10,
        )

    @task(3)
    def ingredients(self):
        self.client.get(
            "/api/ingredients/?name=абрикос",
            headers=DEFAULT_HEADERS,
            name="/api/ingredients/",
            timeout=10,
        )

    @task(2)
    def users(self):
        self.client.get(
            "/api/users/?page=1&limit=6",
            headers=DEFAULT_HEADERS,
            name="/api/users/",
            timeout=10,
        )
