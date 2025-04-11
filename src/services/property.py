from typing import Optional, Union
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from constants.property import PropertyType
from crud.color import color_crud
from crud.height import height_crud
from crud.memory_size import memory_size_crud
from models import Color, Height, MemorySize
from schemas.color import ColorPaginationResponse, ColorResponse
from schemas.height import HeightPaginationResponse, HeightResponse
from schemas.memory_size import (
    MemorySizePahinationResponse,
    MemorySizeResponse,
)
from schemas.property import PropertyBase
from services import color as color_service
from services import height as height_service
from services import memory_size as memory_size_service


async def create(
    db: AsyncSession, schema: PropertyBase
) -> Optional[Union[Color, Height, MemorySize]]:
    if schema.propetry_type == PropertyType.COLOR:
        try:
            return await color_service.create(db=db, schema=schema)
        except Exception as e:
            raise Exception(str(e))
    if schema.propetry_type == PropertyType.HIGHT:
        try:
            return await height_service.create(db=db, schema=schema)
        except Exception as e:
            raise Exception(str(e))
    if schema.propetry_type == PropertyType.MEMORY_SIZE:
        try:
            return await memory_size_service.create(db=db, schema=schema)
        except Exception as e:
            raise Exception(str(e))


async def read(
    db: AsyncSession,
    prooerty_type: PropertyType,
    skip: int = 0,
    limit: int = 10,
) -> Union[
    ColorPaginationResponse,
    HeightPaginationResponse,
    MemorySizePahinationResponse,
]:
    if prooerty_type == PropertyType.COLOR:
        return await color_crud.get_multi(db=db, skip=skip, limit=limit)
    if prooerty_type == PropertyType.HIGHT:
        return await height_crud.get_multi(db=db, skip=skip, limit=limit)
    if prooerty_type == PropertyType.MEMORY_SIZE:
        return await memory_size_crud.get_multi(db=db, skip=skip, limit=limit)


async def read_by_uid(db: AsyncSession, uid: UUID) -> Optional[dict[str, str]]:
    if found_color := await color_crud.get_by_uid(db=db, uid=uid):
        return {"type": PropertyType.COLOR, "object": ColorResponse}
    if found_height := await height_crud.get_by_uid(db=db, uid=uid):
        return {"type": PropertyType.HIGHT, "object": HeightResponse}
    if found_memory_size := await memory_size_crud.get_by_uid(db=db, uid=uid):
        return {"type": PropertyType.MEMORY_SIZE, "object": MemorySizeResponse}
    if not found_color and not found_height and not found_memory_size:
        raise Exception("Not found")
