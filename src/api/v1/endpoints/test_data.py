from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from utilities import test_data

router = APIRouter()


@router.get("/properties/", status_code=status.HTTP_200_OK)
async def get_test_properties(db: AsyncSession = Depends(get_async_db)):
    await test_data.create_test_properties(db=db)


@router.get("/products/", status_code=status.HTTP_200_OK)
async def get_test_products(db: AsyncSession = Depends(get_async_db)):
    await test_data.create_test_products(db=db)
