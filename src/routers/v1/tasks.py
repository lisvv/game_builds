from fastapi import APIRouter, Depends, Request
from schemas.builds import InputSchema
from application.dependencies import get_task_service
from application.dependencies import get_build_service

tasks_router = APIRouter(prefix="")


success = {"content": {"application/json": {"example": ["dependency-1", "dependency-2", "task1"]}}}
not_found = {"content": {"application/json": {"example": {"message": "build not found"}}}}


@tasks_router.post("/get_tasks", responses={200: success, 404: not_found})
async def get_tasks(
        request: Request,
        input: InputSchema,
        build_service=Depends(get_build_service),
        tasks_service=Depends(get_task_service)
) -> list[str]:
    """Returns list of tasks"""
    build = await build_service.get_build(build_name=input.build, builds=request.app.state.BUILDS)
    return await tasks_service.handle_task_list(tasks_list=build.tasks, tasks=request.app.state.TASKS)