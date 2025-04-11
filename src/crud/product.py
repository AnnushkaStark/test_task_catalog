from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from crud.async_crud import BaseAsyncCRUD
from models import Product
from schemas.product import ProductBase, ProductCreate


class ProductCRUD(BaseAsyncCRUD[Product, ProductBase, ProductCreate]):
    async def get_by_uid(
        self, db: AsyncSession, uid: UUID
    ) -> Optional[Product]:
        statement = select(self.model).options(
            joinedload(self.model.heights),
            joinedload(self.model.colors),
            joinedload(self.model.memory_sizes),
        )
        result = await db.execute(statement)
        return result.scalars().unique().first()


product_crud = ProductCRUD(Product)
