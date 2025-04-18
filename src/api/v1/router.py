from fastapi import APIRouter

from api.v1.endpoints.product import router as product_router
from api.v1.endpoints.property import router as prpperty_router
from api.v1.endpoints.test_data import router as test_data_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    test_data_router, prefix="/test_data", tags=["TestData"]
)
api_router.include_router(
    prpperty_router, prefix="/property", tags=["Property"]
)
api_router.include_router(product_router, prefix="/product", tags=["Product"])
