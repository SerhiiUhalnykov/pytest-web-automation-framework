import pytest
import allure
from playwright.sync_api import Page

from pages.dynamic_loading_page import DynamicLoadingPage


@allure.feature("Loading")
@allure.story("Dynamic Loading behavior")
@pytest.mark.slow
@pytest.mark.regression
class TestDynamicLoading:
    def test_hidden_element(self, page: Page) -> None:

        loading_page = DynamicLoadingPage(page)
        loading_page.open_example(1)

        loading_page.start_loading()
        loading_page.assert_loading_then_done(10_000)
        loading_page.assert_finish_text()

    def test_element_added_after(self, page: Page) -> None:

        loading_page = DynamicLoadingPage(page)
        loading_page.open_example(2)

        loading_page.start_loading()
        loading_page.assert_loading_then_done(10_000)
        loading_page.assert_finish_text()
