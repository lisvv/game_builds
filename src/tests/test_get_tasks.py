from fastapi.testclient import TestClient

from application.app import init_app
from dto.builds import BuildDTO
from dto.tasks import InputTaskDTO

app = init_app()


def test_build_success_if_tasks_is_exists():
    build_name = "new_build"
    task1_name = "new_task1"
    task2_name = "new_task2"

    app.state.BUILDS = {
        build_name: BuildDTO(name=build_name, tasks=[task1_name, task2_name])
    }
    app.state.TASKS = {
        task1_name: InputTaskDTO(name=task1_name, dependencies=[]),
        task2_name: InputTaskDTO(name=task2_name, dependencies=[]),
    }
    client = TestClient(app)

    response = client.post("/api/v1/get-tasks/", json={"build": build_name})

    assert response.status_code == 200
    assert response.json() == [task1_name, task2_name]


def test_404_if_build_not_exists():
    build_name = "new_build"
    task1_name = "new_task1"
    task2_name = "new_task2"
    undefined_build = "some_another_build"

    app.state.BUILDS = {
        build_name: BuildDTO(name=build_name, tasks=[task1_name, task2_name])
    }
    app.state.TASKS = {
        task1_name: InputTaskDTO(name=task1_name, dependencies=[]),
        task2_name: InputTaskDTO(name=task2_name, dependencies=[]),
    }
    client = TestClient(app)

    response = client.post("/api/v1/get-tasks/", json={"build": undefined_build})

    assert response.status_code == 404
    assert response.json() == {"detail": f"Build {undefined_build} not found"}


def test_404_if_tasks_in_build_not_exists():
    build_name = "new_build"
    task1_name = "new_task1"
    task2_name = "new_task2"
    undefined_task = "undefined_task"

    app.state.BUILDS = {
        build_name: BuildDTO(name=build_name, tasks=[task1_name, undefined_task])
    }
    app.state.TASKS = {
        task1_name: InputTaskDTO(name=task1_name, dependencies=[]),
        task2_name: InputTaskDTO(name=task2_name, dependencies=[]),
    }
    client = TestClient(app)

    response = client.post("/api/v1/get-tasks/", json={"build": build_name})

    assert response.status_code == 404
    assert response.json() == {"detail": f"Tasks: { {undefined_task} } not found"}


def test_success_with_dependencies():
    build_name = "new_build"
    task1_name = "new_task1"
    task2_name = "new_task2"
    task3_name = "new_task3"
    task4_name = "new_task4"
    task5_name = "new_task5"

    app.state.BUILDS = {build_name: BuildDTO(name=build_name, tasks=[task1_name])}
    app.state.TASKS = {
        task1_name: InputTaskDTO(name=task1_name, dependencies=[task2_name]),
        task2_name: InputTaskDTO(name=task2_name, dependencies=[task3_name]),
        task3_name: InputTaskDTO(
            name=task3_name, dependencies=[task4_name, task5_name]
        ),
        task4_name: InputTaskDTO(name=task4_name, dependencies=[]),
        task5_name: InputTaskDTO(name=task5_name, dependencies=[]),
    }
    client = TestClient(app)

    response = client.post("/api/v1/get-tasks/", json={"build": build_name})

    assert response.status_code == 200
    assert response.json() == [
        task4_name,
        task5_name,
        task3_name,
        task2_name,
        task1_name,
    ]
