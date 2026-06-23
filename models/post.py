from models.base import BaseModel
from models.base import NonEmptyBaseModel


class ReactionsResponse(NonEmptyBaseModel):
    _check_non_empty = {"likes", "dislikes"}

    likes: int
    dislikes: int


class PostResponse(NonEmptyBaseModel):
    _check_non_empty = {"id", "userId"}

    id: int
    userId: int
    title: str
    body: str
    tags: list[str]
    reactions: ReactionsResponse | None = None
    views: int | None = None
    isDeleted: bool | None = None
    deletedOn: str | None = None


class PostsResponse(NonEmptyBaseModel):
    _check_non_empty = {"total", "skip", "limit"}

    posts: list
    total: int
    skip: int
    limit: int


class PostRequest(BaseModel):
    userId: int | None = None
    title: str | None = None
    body: str | None = None
    tags: list[str] | None = None
