import requests

import allure

from api.base_client import BaseClient


class UserClient(BaseClient):
    CLIENT_PATH: str = "/user"

    @allure.step("Get current auth user")
    def get_auth_user(self) -> requests.Response:
        return self.get("/me")
