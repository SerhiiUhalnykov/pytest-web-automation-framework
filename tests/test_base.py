import pytest
import allure
from playwright.sync_api import Page

from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_main(page: Page) -> None:
    base = BasePage(page)
    base.open()

    assert base.page.title() == "The Internet"