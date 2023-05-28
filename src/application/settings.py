from pydantic import BaseSettings
import os
from pathlib import Path


class Settings(BaseSettings):
    DEBUG: bool = True
    RELOAD: bool = True
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    BUILDS_DIR: str = "builds"
    TASKS_FILENAME: str = "tasks.yaml"
    BUILDS_FILENAME: str = "builds.yaml"
    ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
