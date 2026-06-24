from models.base import BaseModel
from models.base import NonEmptyBaseModel


class ReactionsResponse(NonEmptyBaseModel):
    """Nested reactions object within a post response."""

    _check_non_empty = {"likes", "dislikes"}

    likes: int
    dislikes: int


class PostResponse(NonEmptyBaseModel):
    """Response body for a single post."""

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
    """Response body for the paginated posts list."""

    _check_non_empty = {"total", "skip", "limit"}

    posts: list[PostResponse]
    total: int
    skip: int
    limit: int


class PostRequest(BaseModel):
    """Request body for create and update post operations."""

    userId: int | None = None
    title: str | None = None
    body: str | None = None
    tags: list[str] | None = None
