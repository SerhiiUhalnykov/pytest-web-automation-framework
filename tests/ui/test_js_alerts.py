import pytest
import allure
from playwright.sync_api import Page
from faker import Faker

from pages.js_alerts_page import JSAlertsPage

fake = Faker()


@allure.feature("Alerts")
@allure.story("JavaScript Alerts behavior")
@pytest.mark.regression
class TestJSAlerts:
    def test_alert(self, page: Page) -> None:

        alert_page = JSAlertsPage(page)
        alert_page.open()
        alert_page.assert_loaded()

        alert_page.trigger_alert("alert", True, None)
        alert_page.assert_result_text("You successfully clicked an alert")

    def test_confirm(self, page: Page) -> None:

        alert_page = JSAlertsPage(page)
        alert_page.open()
        alert_page.assert_loaded()

        alert_page.trigger_alert("confirm", True, None)
        alert_page.assert_result_text("You clicked: Ok")
        alert_page.trigger_alert("confirm", False, None)
        alert_page.assert_result_text("You clicked: Cancel")

    def test_prompt(self, page: Page) -> None:

        alert_page = JSAlertsPage(page)
        alert_page.open()
        alert_page.assert_loaded()

        text = fake.word()
        alert_page.trigger_alert("prompt", True, text)
        alert_page.assert_result_text(f"You entered: {text}")
        alert_page.trigger_alert("prompt", False, text)
        alert_page.assert_result_text("You entered: null")
