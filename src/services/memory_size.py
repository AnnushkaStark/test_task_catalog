from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from crud.memory_size import memory_size_crud
from models import MemorySize
from schemas.memory_size import MemmorySizeBase
from schemas.property import PropertyBase


async def create(
    db: AsyncSession, schema: PropertyBase
) -> Optional[MemorySize]:
    if await memory_size_crud.get_by_value(db=db, value=schema.value):
        raise Exception("Memory size alredy exsist")
    create_schema = MemmorySizeBase(value=schema.value)
    return await memory_size_crud.create(db=db, create_schema=create_schema)
