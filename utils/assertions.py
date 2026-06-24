from typing import TypeVar, Any

import allure
import requests
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


@allure.step("Validate response status code")
def assert_status_code(code: int, expected: int) -> None:
    """Assert actual status code equals the expected code."""

    assert code == expected, (
        f"Expected status code: {expected}, received: {code}"
    )


@allure.step("Validate response schema")
def assert_valid_schema(body: dict, model: type[T]) -> T:
    """Validate body against a Pydantic model and return the parsed instance."""

    return model.model_validate(body)


@allure.step("Validate field")
def assert_valid_field(model: BaseModel, field: str, expected: object) -> None:
    """Assert a parsed model field equals the expected value."""

    value = getattr(model, field)
    assert value == expected, f"Expected {field}={expected!r}, got {value!r}"


@allure.step("Validate response contains payload")
def assert_response_contains_payload(
    body: dict[str, Any], model: BaseModel
) -> None:
    """Assert all non-None model fields are present in the response body."""

    for key, value in model.model_dump(exclude_none=True).items():
        assert body.get(key) == value, (
            f"{key}: expected {value!r}, got {body.get(key)!r}"
        )


@allure.step("Validate response time")
def assert_response_time(
    response: requests.Response, max_seconds: float = 2.0
) -> None:
    """Assert the response elapsed time is within max_seconds."""

    actual_time = response.elapsed.total_seconds()
    assert actual_time <= max_seconds, (
        f"Actual response time {actual_time:.2f}s, expected under {max_seconds}s"
    )
