import pytest
import allure

from api.posts_client import PostsClient
from models.post import PostsResponse
from utils.assertions import assert_status_code, assert_valid_schema


@allure.feature("Demo")
@pytest.mark.demo
class TestApiDemoReport:
    """Deliberately non-passing API tests that populate every Allure status
    (skipped / failed / broken) for the demo report. Marked `demo` only.
    """

    @pytest.mark.skip(reason="Demo: skipped state (grey) in the Allure report")
    def test_demo_skipped(self) -> None:
        pass

    def test_demo_failed(self, posts_client: PostsClient) -> None:
        """AssertionError -> 'failed' (red). Attaches the response JSON."""

        response = posts_client.get_all_posts()
        assert_status_code(response.status_code, 999)

    def test_demo_broken(self, posts_client: PostsClient) -> None:
        """ValidationError -> 'broken' (yellow) -> schema-mismatch category."""

        response = posts_client.get_post(1)
        assert_valid_schema(response.json(), PostsResponse)
