import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    """Page object for the /basic_auth endpoint."""

    PATH: str = "/basic_auth"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._heading = self._page.get_by_role("heading", name="Basic Auth")
        self._auth_pass_text = self._page.get_by_text(
            "Congratulations! You must have the proper credentials."
        )
        self._auth_fail_text = self._page.get_by_text("Not authorized")

    @allure.step("Check Basic Auth page is loaded")
    def assert_loaded(self) -> None:
        """Assert all Basic Auth page elements are visible"""

        expect(self._heading).to_be_visible()
        expect(self._auth_pass_text).to_be_visible()

    @allure.step("Check Basic Auth fail message")
    def assert_fail_message(self) -> None:
        """Assert Basic Auth fail message is visible"""

        expect(self._auth_fail_text).to_be_visible()
