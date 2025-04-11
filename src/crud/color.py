from crud.async_crud import BaseAsyncCRUD
from models import Color
from schemas.color import ColorBase, ColorResponse


class ColorCRUD(BaseAsyncCRUD[Color, ColorBase, ColorResponse]):
    pass


color_crud = ColorCRUD(Color)
