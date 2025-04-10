from typing import List
from uuid import UUID

from pydantic import BaseModel

from schemas.pagination import PaginatedResponseBase


class MemmorySizeBase(BaseModel):
    value: int


class MemorySizeResponse(MemmorySizeBase):
    id: int
    uid: UUID


class MemorySizePahinationResponse(PaginatedResponseBase):
    objects: List[MemorySizeResponse]
