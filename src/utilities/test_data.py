from sqlalchemy.ext.asyncio import AsyncSession

from constants.property import PropertyType
from schemas.product import ProductCreate
from schemas.property import PropertyBase
from services import product as product_service
from services import property as propery_service


async def create_test_properties(db: AsyncSession):
    properties = [
        PropertyBase(propetry_type=PropertyType.COLOR, value="F000"),
        PropertyBase(propetry_type=PropertyType.COLOR, value="F001"),
        PropertyBase(propetry_type=PropertyType.COLOR, value="F002"),
        PropertyBase(propetry_type=PropertyType.HIGHT, value="1"),
        PropertyBase(propetry_type=PropertyType.HIGHT, value="2"),
        PropertyBase(propetry_type=PropertyType.HIGHT, value="3"),
        PropertyBase(propetry_type=PropertyType.MEMORY_SIZE, value="5mb"),
        PropertyBase(propetry_type=PropertyType.MEMORY_SIZE, value="10mb"),
        PropertyBase(propetry_type=PropertyType.MEMORY_SIZE, value="15mb"),
    ]
    for property in properties:
        await propery_service.create(db=db, schema=property)


async def create_test_products(db: AsyncSession):
    products = [
        ProductCreate(
            name="FirstProduct",
            colors_ids=[1, 2, 3],
            heigts_ids=[],
            memory_sizes_ids=[],
        ),
        ProductCreate(
            name="SecondProduct",
            colors_ids=[],
            heigts_ids=[1, 2, 3],
            memory_sizes_ids=[],
        ),
        ProductCreate(
            name="ThirdProduct",
            colors_ids=[],
            heigts_ids=[],
            memory_sizes_ids=[1, 2, 3],
        ),
    ]
    for product in products:
        await product_service.create(db=db, create_schema=product)
