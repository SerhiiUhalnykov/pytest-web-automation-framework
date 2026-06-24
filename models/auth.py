from models.base import NonEmptyBaseModel


class LoginResponse(NonEmptyBaseModel):
    """Response body for a successful /auth/login request."""

    _check_non_empty = {"accessToken", "refreshToken"}

    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str
    accessToken: str
    refreshToken: str
