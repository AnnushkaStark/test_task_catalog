from fastapi import APIRouter

from api.v1.endpoints.property import router as prpperty_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    prpperty_router, prefix="/property", tags=["Property"]
)
