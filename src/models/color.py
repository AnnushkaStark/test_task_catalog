import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import UUID, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

from .m2m import ProductColor

if TYPE_CHECKING:
    from .product import Product


class Color(Base):
    """
    Модель цвета

    ## Attrs:
      - id: int - идентификатор
      - uid: UUID - идентификатор
      - value: str - обозначение цвета в RGB
      - products: List[Product] - связь с продуктами
    """

    __tablename__ = "color"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    value: Mapped[str] = mapped_column(String, unique=True)
    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="colors", secondary=ProductColor.__table__
    )
