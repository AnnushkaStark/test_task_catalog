from crud.async_crud import BaseAsyncCRUD
from models import Height
from schemas.height import HeihgtBase


class HeightCRUD(BaseAsyncCRUD[Height, HeihgtBase]):
    pass


height_crud = HeightCRUD(Height)
