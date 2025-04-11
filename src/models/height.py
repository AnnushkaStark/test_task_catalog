import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import UUID, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

from .m2m import ProductHeight

if TYPE_CHECKING:
    from .product import Product


class Height(Base):
    """
    Модель высоты

    ## Attrs:
        - id: int - идентифкатор
        - uid: UUID - идентификатор
        - value: int - высота
        - products: List[Product] - связь с продуктами
    """

    __tablename__ = "height"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    value: Mapped[str] = mapped_column(String, unique=True)
    products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="heights", secondary=ProductHeight.__table__
    )
