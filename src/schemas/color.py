from typing import List
from uuid import UUID

from pagination import PaginatedResponseBase
from pydantic import BaseModel


class ColorBase(BaseModel):
    value: str


class ColorResponse(ColorBase):
    id: int
    uid: UUID


class ColorPaginationResponse(PaginatedResponseBase):
    object: List[ColorResponse]
