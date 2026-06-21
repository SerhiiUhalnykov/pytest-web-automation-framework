from models.base import NonEmptyBaseModel


class LoginResponse(NonEmptyBaseModel):
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
