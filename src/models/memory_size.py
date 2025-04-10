import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import UUID, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.database import Base

from .m2m import ProductMemorySize

if TYPE_CHECKING:
    from .product import Product


class MemorySize(Base):
    """
    Mодель объемов памяти
    ## Attrs:
        - id: int - идентификатор
        - uid: UUID -идентификатор
        - value: int -объем памяти
        - products: List[Product] - связь с продуктами

    """

    __tablename__ = "memory_size"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID, unique=True, index=True, default=uuid.uuid4
    )
    value: Mapped[int]
    products: Mapped[List["Product"]] = relationship(
        "Product",
        back_populates="memory_sizes",
        secondary=ProductMemorySize.__table__,
    )
