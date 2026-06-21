from models.base import NonEmptyBaseModel


class UserResponse(NonEmptyBaseModel):
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
