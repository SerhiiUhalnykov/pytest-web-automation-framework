from typing import Any

import pytest
import allure
from playwright.sync_api import Page

from pages.basic_auth_page import BasicAuthPage
from data.users import Users


@allure.feature("Authentication")
@allure.story("Basic Auth page behavior")
@pytest.mark.regression
class TestBasicAuth:
    @pytest.fixture()
    def browser_context_args(
        self,
        browser_context_args: dict[str, Any],
        request: pytest.FixtureRequest,
    ) -> dict[str, Any]:
        return {
            **browser_context_args,
            "http_credentials": getattr(request, "param", None),
        }

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "browser_context_args",
        [{"username": Users.ADMIN.username, "password": Users.ADMIN.password}],
        ids=["valid_credentials"],
        indirect=True,
    )
    def test_basic_auth_valid(self, page: Page) -> None:

        basic_auth_page = BasicAuthPage(page)
        basic_auth_page.open()
        basic_auth_page.assert_loaded()

    def test_basic_auth_invalid(self, page: Page) -> None:

        basic_auth_page = BasicAuthPage(page)
        basic_auth_page.open()
        basic_auth_page.assert_fail_message()
