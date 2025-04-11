from crud.async_crud import BaseAsyncCRUD
from models import MemorySize
from schemas.memory_size import MemmorySizeBase, MemorySizeResponse


class MemmorySizeCRUD(
    BaseAsyncCRUD[MemorySize, MemmorySizeBase, MemorySizeResponse]
):
    pass


memory_size_crud = MemmorySizeCRUD(MemorySize)
