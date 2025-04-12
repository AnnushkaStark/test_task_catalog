from typing import List
from uuid import UUID

from pydantic import BaseModel

from schemas.pagination import PaginatedResponseBase


class ColorBase(BaseModel):
    value: str


class ColorResponse(ColorBase):
    id: int
    uid: UUID


class ColorPaginationResponse(PaginatedResponseBase):
    object: List[ColorResponse]
