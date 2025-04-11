from sqlalchemy.ext.asyncio import AsyncSession

from crud.product import product_crud
from schemas.product import ProductCreate
from utilities import product as product_properties


async def create(db: AsyncSession, create_schema: ProductCreate) -> None:
    try:
        colors = await product_properties.check_colors(
            db=db, schema=create_schema
        )
    except Exception as e:
        raise Exception(str(e))
    del create_schema.colors_ids
    try:
        heights = await product_properties.check_heights(
            db=db, schema=create_schema
        )
    except Exception as e:
        raise Exception(str(e))
    del create_schema.heigts_ids
    try:
        memory_sizes = await product_properties.check_memory_sizes(
            db=db, schema=create_schema
        )
    except Exception as e:
        raise Exception(str(e))
    del create_schema.memory_sizes_ids
    product = await product_crud.create(
        db=db, create_schema=create_schema, commit=False
    )
    product.colors = colors
    product.heights = heights
    product.memory_sizes = memory_sizes
    await db.commit()
