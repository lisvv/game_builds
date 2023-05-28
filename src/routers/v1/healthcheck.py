from fastapi import APIRouter
from fastapi.responses import JSONResponse

healthcheck_router = APIRouter()

RESPONSE = {
    200: {"content": {"application/json": {"example": {"healthcheck": "ok"}}}},
}


@healthcheck_router.get("/healthcheck", responses=RESPONSE)
async def healthcheck() -> JSONResponse:
    """
    Service health check.
    """
    return JSONResponse(content={"healthcheck": "ok"}, status_code=200)
