from typing import Optional, Sequence

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from models import Product
from utilities.search import get_transliterated_value


class ProductFilter(Filter):
    color: Optional[str] = None
    height: Optional[int] = None
    memoty_size: Optional[str] = None

    class Constants(Filter.Constants):
        model = Product

    async def filter(
        self,
        db: AsyncSession,
        query: Optional[str] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> Sequence[Product]:
        statement = (
            select(Product, func.count().over().label("total"))
            .options(
                joinedload(Product.colors),
                joinedload(Product.heights),
                joinedload(Product.memory_sizes),
            )
            .offset(skip)
            .limit(limit)
        )
        if query is not None:
            lst_query = await get_transliterated_value(query=query)
            statement = statement.where(
                or_(*[Product.name.ilike(f"%{q}%") for q in lst_query])
            )
        if self.color is not None:
            statement = statement.where(Product.colors.any(value=self.color))
        if self.height is not None:
            statement = statement.where(Product.heights.any(value=self.height))
        if self.memoty_size is not None:
            statement = statement.where(
                Product.memory_sizes.any(value=self.memoty_size)
            )
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["Product"] for r in rows],
        }
