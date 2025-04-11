from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from crud.color import color_crud
from models import Color
from schemas.color import ColorBase
from schemas.property import PropertyBase


async def create(db: AsyncSession, schema: PropertyBase) -> Optional[Color]:
    if await color_crud.get_by_value(db=db, value=schema.value):
        raise Exception("Color alredy exsist")
    create_schema = ColorBase(value=schema.value)
    return await color_crud.create(db=db, create_schema=create_schema)
