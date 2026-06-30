import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class UploadPage(BasePage):
    """Page object for the /upload endpoint."""

    PATH: str = "/upload"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._file_input = self._page.locator(
            "input[type='file'][id='file-upload']"
        )
        self._header_upload = self._page.get_by_role(
            "heading", name="File Uploader"
        )
        self._header_success = self._page.get_by_role(
            "heading", name="File Uploaded!"
        )
        self._header_failed = self._page.get_by_role(
            "heading", name="Internal Server Error"
        )
        self._btn = self._page.get_by_role("button", name="Upload")

    @allure.step("Check upload page is loaded")
    def assert_loaded(self) -> None:
        """Assert UploadPage elements are visible."""

        expect(self._header_upload).to_be_visible()
        expect(self._btn).to_be_visible()

    @allure.step("Choose a text file to download with give name and text")
    def choose_inmemory_file(self, name: str, text: str) -> None:
        """Make a test in-memory file with given name and text.
        Choose it for uploading.
        """

        logger.info(f"Create and choose text file {name}.txt for uploading")
        self._file_input.set_input_files({
            "name": f"{name}.txt",
            "mimeType": "text/plain",
            "buffer": text.encode("utf-8"),
        })

    @allure.step("Upload chosen file")
    def upload_file(self) -> None:
        """Trigger the button to upload chosen file."""

        self._btn.click()

    @allure.step("Check that chosen file is uploaded")
    def assert_file_uploaded(self, name: str) -> None:
        """Assert elements for successful file uploading are visible."""

        expect(self._header_success).to_be_visible()
        expect(self._page.get_by_text(f"{name}.txt")).to_be_visible()

    @allure.step("Check that file uploading failed")
    def assert_upload_failed(self) -> None:
        """Assert elements for unsuccessful file uploading are visible."""

        expect(self._header_failed).to_be_visible()
