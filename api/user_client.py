import requests

import allure

from api.base_client import BaseClient


class UserClient(BaseClient):
    """Client for the /user API endpoints."""

    CLIENT_PATH: str = "/user"

    @allure.step("Get current auth user")
    def get_auth_user(self) -> requests.Response:
        """Fetch the current user using the session auth token."""

        return self.get("/me")
