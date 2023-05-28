from fastapi import HTTPException

from dto.tasks import InputTaskDTO


class TaskService:
    def __init__(self):
        self.dependencies: list[str] = []

    async def handle_task_list(
        self, tasks_list: list[str], tasks: dict[str, InputTaskDTO]
    ) -> list[str]:
        unexpected_tasks = set(tasks_list) - set(tasks.keys())
        if unexpected_tasks:
            raise HTTPException(
                status_code=404, detail=f"Tasks: {unexpected_tasks} not found"
            )
        for task_name in tasks_list:
            task = tasks.get(task_name)
            if task.dependencies:
                await self.handle_task_list(task.dependencies, tasks)
            self.dependencies.append(task.name)
        return self.dependencies
