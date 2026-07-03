import pytest
import allure
from playwright.sync_api import Page, expect

from pages.main_page import MainPage


@allure.feature("Demo")
@pytest.mark.demo
class TestUiDemoReport:
    """Deliberately non-passing UI tests that populate every Allure status
    (skipped / failed / broken) for the demo report. Marked `demo` only.
    """

    @pytest.mark.skip(reason="Demo: skipped state (grey) in the Allure report")
    def test_demo_skipped(self) -> None:
        pass

    def test_demo_failed(self, page: Page) -> None:
        """AssertionError -> 'failed' (red). Attaches screenshot + trace."""

        MainPage(page).open()
        expect(page).to_have_title("Intentionally wrong title", timeout=500)

    def test_demo_broken(self, page: Page) -> None:
        """TimeoutError -> 'broken' (yellow) -> UI-timeout category."""

        MainPage(page).open()
        page.locator("#this-element-does-not-exist").click(timeout=500)
