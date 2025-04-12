import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import UUID, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

from .m2m import ProductColor, ProductHeight, ProductMemorySize

if TYPE_CHECKING:
    from .color import Color
    from .height import Height
    from .memory_size import MemorySize


class Product(Base):
    """
    Модель продукта

    ## Attrs:
      - id: int - идентификатор
      - uid: UUID - идентификатор
      - name: str - название
      - colors: List[Color] - связь с цветами
      - hrights: List[Height] - связь с высотой
      - memory_sizes: List[MemorySize] - связь
        с объемами памяти
    """

    __tablename__ = "product"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, index=True)
    colors: Mapped[List["Color"]] = relationship(
        "Color", back_populates="products", secondary=ProductColor.__table__
    )
    heights: Mapped[List["Height"]] = relationship(
        "Height", back_populates="products", secondary=ProductHeight.__table__
    )
    memory_sizes: Mapped[List["MemorySize"]] = relationship(
        "MemorySize",
        back_populates="products",
        secondary=ProductMemorySize.__table__,
    )
