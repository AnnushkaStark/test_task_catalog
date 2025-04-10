from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from constants.product import MAX_LENGTH_NAME, MIN_LENGTH_NAME
from schemas.color import ColorResponse
from schemas.height import HeightResponse
from schemas.memory_size import MemorySizeResponse
from schemas.pagination import PaginatedResponseBase


class ProductBase(BaseModel):
    name: str = Field(max_length=MAX_LENGTH_NAME, min_length=MIN_LENGTH_NAME)


class ProductCreate(ProductBase):
    colors_ids: Optional[List[int]] = []
    heigts_ids: Optional[List[int]] = []
    memory_sizes_ids: Optional[List[int]] = []


class ProductResponse(ProductBase):
    id: int
    uid: UUID
    colors: List[ColorResponse] = []
    heights: List[HeightResponse] = []
    memory_sizes: List[MemorySizeResponse] = []


class ProductPaginationResponse(PaginatedResponseBase):
    objects: List[ProductResponse]
