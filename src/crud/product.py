from typing import Optional
from uuid import UUID

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from crud.async_crud import BaseAsyncCRUD
from models import Product
from schemas.product import ProductBase


class ProductCRUD(BaseAsyncCRUD[Product, ProductBase]):
    async def get_by_uid(
        self, db: AsyncSession, uid: UUID
    ) -> Optional[Product]:
        statement = (
            select(self.model)
            .options(
                joinedload(self.model.heights),
                joinedload(self.model.colors),
                joinedload(self.model.memory_sizes),
            )
            .where(self.model.uid == uid)
        )
        result = await db.execute(statement)
        return result.scalars().unique().first()

    async def create(
        self,
        db: AsyncSession,
        create_schema: ProductBase,
        commit: bool = True,
    ) -> Product:
        data = create_schema.model_dump(exclude_unset=True)
        stmt = (
            insert(self.model)
            .values(**data)
            .returning(self.model)
            .options(
                selectinload(self.model.heights),
                selectinload(self.model.colors),
                selectinload(self.model.memory_sizes),
            )
        )
        res = await db.execute(stmt)
        if commit:
            await db.commit()
        return res.scalars().first()


product_crud = ProductCRUD(Product)
