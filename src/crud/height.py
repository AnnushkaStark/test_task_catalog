from crud.async_crud import BaseAsyncCRUD
from models import Height
from schemas.height import HeightResponse, HeihgtBase


class HeightCRUD(BaseAsyncCRUD[Height, HeihgtBase, HeightResponse]):
    pass


height_crud = HeightCRUD(HeightResponse)
