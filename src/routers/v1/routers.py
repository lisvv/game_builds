from fastapi import APIRouter

from routers.v1 import healthcheck
from routers.v1 import tasks

router = APIRouter(prefix="/api/v1")

router.include_router(healthcheck.healthcheck_router, tags=["healthcheck"])
router.include_router(tasks.tasks_router, tags=["builds"])
