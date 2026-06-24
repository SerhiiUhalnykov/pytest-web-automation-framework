from pydantic import BaseModel


class TestUser(BaseModel):
    """Holds username and password for a test account."""

    username: str
    password: str
