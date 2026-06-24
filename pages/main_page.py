import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class MainPage(BasePage):
    """Page object for the home page at /."""

    PATH: str = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._heading = self._page.get_by_role(
            "heading", name="Welcome to the-internet"
        )

    @allure.step("Check main page is loaded")
    def assert_loaded(self) -> None:
        """Assert the welcome heading is visible."""

        expect(self._heading).to_be_visible()
