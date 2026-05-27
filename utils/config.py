import os

from dotenv import load_dotenv

load_dotenv()

URL: str = os.getenv("URL", "")
USERNAME: str = os.getenv("USERNAME", "")
PASSWORD: str = os.getenv("PASSWORD", "")