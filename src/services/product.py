from sqlalchemy.ext.asyncio import AsyncSession

from crud.product import product_crud
from schemas.product import ProductBase, ProductCreate
from utilities import product as product_properties


async def create(db: AsyncSession, create_schema: ProductCreate) -> None:
    try:
        colors = await product_properties.check_colors(
            db=db, schema=create_schema
        )
        heights = await product_properties.check_heights(
            db=db, schema=create_schema
        )
        memory_sizes = await product_properties.check_memory_sizes(
            db=db, schema=create_schema
        )
    except Exception as e:
        raise Exception(str(e))
    create_data = ProductBase(name=create_schema.name)
    product = await product_crud.create(
        db=db, create_schema=create_data, commit=False
    )
    product.colors = colors
    product.heights = heights
    product.memory_sizes = memory_sizes
    await db.commit()
