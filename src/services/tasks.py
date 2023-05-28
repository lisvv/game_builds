from dto.builds import BuildDTO
from dto.tasks import InputTaskDTO


class TaskService:

    def __init__(self):
        self.dependencies: list[str] = []

    async def handle_task_list(self, tasks_list: list[str], tasks: dict[str, InputTaskDTO]) -> list[str]:
        for task_name in tasks_list:
            task = tasks.get(task_name)
            if task.dependencies:
                await self.handle_task_list(task.dependencies, tasks)
            self.dependencies.append(task.name)
        return self.dependencies
