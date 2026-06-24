from models.test_user import TestUser
from utils.config import settings


class Users:
    """Registry of pre-configured test users loaded from settings."""

    STAN = TestUser(username=settings.user_stan, password=settings.pass_stan)
    ADMIN = TestUser(
        username=settings.user_admin, password=settings.pass_admin
    )
    API = TestUser(username=settings.user_api, password=settings.pass_api)
