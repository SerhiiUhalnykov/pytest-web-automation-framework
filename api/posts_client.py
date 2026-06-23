import requests

import allure

from api.base_client import BaseClient
from models.post import PostRequest


class PostsClient(BaseClient):
    CLIENT_PATH: str = "/posts"

    @allure.step("Get post by id")
    def get_post(self, id: int) -> requests.Response:
        return self.get(f"/{id}")

    @allure.step("Get all posts")
    def get_all_posts(self) -> requests.Response:
        return self.get()

    @allure.step("Add new post")
    def create_post(self, payload: PostRequest) -> requests.Response:
        return self.post("/add", json=payload.model_dump(exclude_none=True))

    @allure.step("Update post full")
    def update_post_full(
        self, id: int, payload: PostRequest
    ) -> requests.Response:
        return self.put(f"/{id}", json=payload.model_dump(exclude_none=True))

    @allure.step("Update post partial")
    def update_post_partial(
        self, id: int, payload: PostRequest
    ) -> requests.Response:
        return self.patch(f"/{id}", json=payload.model_dump(exclude_none=True))

    @allure.step("Delete post")
    def delete_post(self, id: int) -> requests.Response:
        return self.delete(f"/{id}")
