from typing import List, Union

from sqlalchemy.ext.asyncio import AsyncSession

from crud.color import color_crud
from crud.height import height_crud
from crud.memory_size import memory_size_crud
from models import Color, Height, MemorySize
from schemas.product import ProductCreate


async def check_colors(
    db: AsyncSession, schema: ProductCreate
) -> Union[List[Color], List, None]:
    if schema.colors_ids != []:
        if len(set(schema.colors_ids)) < len(schema.colors_ids):
            raise Exception("Only unique colors_ids is valid")
        found_colors = await color_crud.get_multi_by_ids(
            db=db, ids=schema.colors_ids
        )
        if len(found_colors) < schema.colors_ids:
            raise Exception("Not all colors was found")
        return found_colors
    return []


async def check_heights(
    db: AsyncSession, schema: ProductCreate
) -> Union[List[Height], List, None]:
    if schema.heigts_ids != []:
        if len(set(schema.heigts_ids)) < len(schema.heigts_ids):
            raise Exception("Only unique heights_ids is valid")
        found_height = await height_crud.get_multi_by_ids(
            db=db, ids=schema.heigts_ids
        )
        if len(found_height) < schema.heigts_ids:
            raise Exception("Not all heights was found")
        return found_height
    return []


async def check_memory_sizes(
    db: AsyncSession, schema: ProductCreate
) -> Union[List[MemorySize], List, None]:
    if schema.memory_sizes_ids != []:
        if len(set(schema.memory_sizes_ids)) < len(schema.memory_sizes_ids):
            raise Exception("Only unique memory_sizes_ids is valid")
        found_memory_sizes = await memory_size_crud.get_multi_by_ids(
            db=db, ids=schema.memory_sizes_ids
        )
        if len(found_memory_sizes) < schema.memory_sizes_ids:
            raise Exception("Not all memory sizes was found")
        return found_memory_sizes
    return []
