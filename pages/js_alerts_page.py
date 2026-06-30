from typing import Literal

import allure
from playwright.sync_api import Page, Dialog, expect

from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

AlertType = Literal["alert", "confirm", "prompt"]


class JSAlertsPage(BasePage):
    """Page object for the /javascript_alerts endpoint."""

    PATH: str = "/javascript_alerts"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._heading = self._page.get_by_role(
            "heading", name="JavaScript Alerts"
        )
        self._alert_btn = self._page.get_by_role(
            "button", name="Click for JS Alert"
        )
        self._confirm_btn = self._page.get_by_role(
            "button", name="Click for JS Confirm"
        )
        self._prompt_btn = self._page.get_by_role(
            "button", name="Click for JS Prompt"
        )
        self._result = self._page.locator("#result")

    @allure.step("Check alerts page is loaded")
    def assert_loaded(self) -> None:
        """Assert JSAlerts page elements are visible"""

        expect(self._heading).to_be_visible()
        expect(self._alert_btn).to_be_visible()
        expect(self._confirm_btn).to_be_visible()
        expect(self._prompt_btn).to_be_visible()

    @allure.step("Trigger specified JS alert")
    def trigger_alert(
        self, alert_type: AlertType, accept: bool, text: str | None
    ) -> None:
        """Trigger a JS dialog and handle it.

        Args:
            alert_type: which dialog button to click ("alert", "confirm", "prompt").
            accept: True to accept (OK), False to dismiss (Cancel).
            text: prompt input text; None for "alert"/"confirm" types.
        """

        def handle_dialog(dialog: Dialog):
            logger.info(
                f"Triggered alert type: {dialog.type}, message: {dialog.message}"
            )
            if accept:
                dialog.accept(text)
            else:
                dialog.dismiss()

        self._page.once("dialog", handle_dialog)

        match alert_type:
            case "alert":
                self._alert_btn.click()
            case "confirm":
                self._confirm_btn.click()
            case "prompt":
                self._prompt_btn.click()
            case _:
                raise ValueError(f"Unsupported alert_type: {alert_type}")

    @allure.step("Check result text")
    def assert_result_text(self, text: str) -> None:
        """Assert the result text after alert handling"""

        expect(self._result).to_contain_text(text)
