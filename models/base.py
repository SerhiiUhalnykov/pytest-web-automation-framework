from typing import ClassVar
from pydantic import BaseModel, model_validator


class NonEmptyBaseModel(BaseModel):
    _check_non_empty: ClassVar[set[str]] = set()

    @model_validator(mode="after")
    def check_non_empty_fields(self) -> "NonEmptyBaseModel":
        for field in self._check_non_empty:
            value = getattr(self, field)
            assert value not in (None, "", [], {}), (
                f"{field} must not be empty, got {value!r}"
            )
        return self


class ErrorResponse(NonEmptyBaseModel):
    _check_non_empty = {"message"}

    message: str
