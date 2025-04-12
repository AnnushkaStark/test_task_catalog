from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from crud.height import height_crud
from models import Height
from schemas.height import HeihgtBase
from schemas.property import PropertyBase


async def create(db: AsyncSession, schema: PropertyBase) -> Optional[Height]:
    if not schema.value.isdigit():
        raise Exception("Invalid height format")
    if await height_crud.get_by_value(db=db, value=int(schema.value)):
        raise Exception("Height alredy exsist")
    create_schema = HeihgtBase(value=int(schema.value))
    return await height_crud.create(db=db, create_schema=create_schema)
