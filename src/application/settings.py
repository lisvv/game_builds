import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    BUILDS_DIR: str = "builds"
    TASKS_FILENAME: str = "tasks.yaml"
    BUILDS_FILENAME: str = "builds.yaml"
    USE_COLORS: bool = True
    ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
