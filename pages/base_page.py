import allure
from playwright.sync_api import Page

from utils.config import URL

class BasePage:
    
    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step("Open page")
    def open(self) -> None:
        self.page.goto(URL)
