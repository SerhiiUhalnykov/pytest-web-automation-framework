from models.base import NonEmptyBaseModel


class UserResponse(NonEmptyBaseModel):
    """Response body for a user profile."""

    _check_non_empty = {
        "id",
        "firstName",
        "lastName",
        "username",
        "password",
        "ip",
        "role",
    }

    id: int
    firstName: str
    lastName: str
    age: int
    gender: str
    email: str
    phone: str
    username: str
    password: str
    ip: str
    role: str
