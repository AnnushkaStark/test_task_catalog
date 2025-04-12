from crud.async_crud import BaseAsyncCRUD
from models import Color
from schemas.color import ColorBase


class ColorCRUD(BaseAsyncCRUD[Color, ColorBase]):
    pass


color_crud = ColorCRUD(Color)
