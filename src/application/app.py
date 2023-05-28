from application.settings import Settings
from fastapi import FastAPI
from routers.v1.routers import router
import yaml
from dto.builds import BuildDTO
from dto.tasks import InputTaskDTO


app_settings = Settings()


def get_builds() -> dict[str, BuildDTO]:
    build_file_path = app_settings.ROOT_DIR.joinpath(app_settings.BUILDS_DIR, app_settings.BUILDS_FILENAME)
    with open(build_file_path) as build_file:
        builds = yaml.safe_load(build_file).get("builds")
        return {build.get("name"): BuildDTO(name=build.get("name"), tasks=build.get("tasks")) for build in builds}


def get_tasks() -> dict[str, InputTaskDTO]:
    task_file_path = app_settings.ROOT_DIR.joinpath(app_settings.BUILDS_DIR, app_settings.TASKS_FILENAME)
    with open(task_file_path) as task_file:
        return {task.get("name"): InputTaskDTO(**task) for task in (yaml.safe_load(task_file).get("tasks"))}


def init_app() -> FastAPI:
    app = FastAPI(dependencies=[])
    app.include_router(
        router,
    )
    app.state.BUILDS = get_builds()
    app.state.TASKS = get_tasks()
    return app

