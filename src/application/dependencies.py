from services.tasks import TaskService
from services.builds import BuildService


def get_task_service() -> TaskService:
    return TaskService()


def get_build_service() -> BuildService:
    return BuildService()
