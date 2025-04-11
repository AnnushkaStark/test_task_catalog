from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from constants.property import PropertyType
from schemas.property import PropertyBase
from services import property as propery_service
from utilities import property

router = APIRouter()


@router.get("/types/", response_model=None)
async def read_property_types():
    return await property.get_property_type()


@router.get("/", response_model=None)
async def read_properties(
    propery_type: PropertyType = Query(...),
    limit: int = 10,
    skip: int = 0,
    db: AsyncSession = Depends(get_async_db),
):
    return await propery_service.read(
        db=db, prooerty_type=propery_type, skip=skip, limit=limit
    )


@router.get("/{property_uid}/", response_model=None)
async def read_property(
    proprty_uid: UUID, db: AsyncSession = Depends(get_async_db)
):
    try:
        return await propery_service.read_by_uid(db=db, uid=proprty_uid)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_property(
    property: PropertyBase,
    db: AsyncSession = Depends(get_async_db),
):
    try:
        return await propery_service.create(db=db, schema=property)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.delete("/{propery_uid}/", status_code=status.HTTP_204_NO_CONTENT)
async def remove_property(
    property_uid: UUID, db: AsyncSession = Depends(get_async_db)
):
    try:
        return await propery_service.delete(db=db, uid=property_uid)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
        )
