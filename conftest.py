"""General fixtures"""

from typing import Iterator

import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def browser() -> Iterator[Browser]:
    
    with sync_playwright() as pw:
        logger.info('Initializing browser session')
        browser = pw.chromium.launch(headless=True)
        
        yield browser

        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Iterator[Page]:

    logger.info('Initializing context')
    context = browser.new_context()
    logger.info('Initializing page')
    page = context.new_page()

    yield page

    context.close()
    page.close()