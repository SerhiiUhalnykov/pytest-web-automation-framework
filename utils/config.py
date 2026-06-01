import os

from dotenv import load_dotenv

load_dotenv()

ARTIFACTS_DIR: str = os.getenv("ARTIFACTS_DIR", "artifacts")

BASE_URL: str = os.getenv("BASE_URL", "")

class Users:
    STAN_USER: str = os.getenv("USER_STAN", "")
    STAN_PASS: str = os.getenv("PASS_STAN", "")

    ADMIN_USER: str = os.getenv("USER_ADMIN", "")
    ADMIN_PASS: str = os.getenv("PASS_ADMIN", "")