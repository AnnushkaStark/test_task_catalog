from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from crud.product import product_crud
from schemas.product import ProductCreate, ProductResponse
from services import product as product_service

router = APIRouter()


@router.get("/{product_uid}/", response_model=ProductResponse)
async def read_product(
    product_uid: UUID, db: AsyncSession = Depends(get_async_db)
):
    if found_product := await product_crud.get_by_uid(db=db, uid=product_uid):
        return found_product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate, db: AsyncSession = Depends(get_async_db)
):
    try:
        return await product_service.create(db=db, create_schema=product)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.delete("/{product_uid}/", status_code=status.HTTP_204_NO_CONTENT)
async def remove_product(
    product_uid: UUID, db: AsyncSession = Depends(get_async_db)
):
    found_product = await product_crud.get_by_uid(db=db, uid=product_uid)
    if not found_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )
    await product_crud.remove(db=db, obj_id=found_product.id)
