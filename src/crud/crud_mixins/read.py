from typing import Any, Generic, List, Optional, Sequence
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from constants.crud_types import ModelType


class ReadAsync(Generic[ModelType]):
    async def get_by_uid(
        self, db: AsyncSession, *, uid: UUID
    ) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.uid == uid)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_multi_by_ids(
        self, db: AsyncSession, *, ids: list[int]
    ) -> List[ModelType]:
        if not ids:
            return []
        statement = select(self.model).where(self.model.id.in_(ids))
        result = await db.execute(statement)
        return result.scalars().all()

    async def get_by_value(
        self, db: AsyncSession, value: Any
    ) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.value == value)
        result = await db.execute(statement)
        return result.scalars().first()

    async def get_multi(
        self, db: AsyncSession, skip: int = 0, limit: int = 10
    ) -> Sequence[ModelType]:
        statement = (
            select(self.model, func.count().over().label("total"))
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(statement)
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r[f"{self.model}"] for r in rows],
        }
