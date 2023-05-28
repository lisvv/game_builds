from services.builds import BuildService
from services.tasks import TaskService


def get_task_service() -> TaskService:
    return TaskService()


def get_build_service() -> BuildService:
    return BuildService()
