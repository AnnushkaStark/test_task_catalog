from typing import List
from uuid import UUID

from pydantic import BaseModel

from schemas.pagination import PaginatedResponseBase


class HeihgtBase(BaseModel):
    value: int


class HeightResponse(HeihgtBase):
    id: int
    uid: UUID


class HeightPaginationResponse(PaginatedResponseBase):
    objects: List[HeightResponse]
