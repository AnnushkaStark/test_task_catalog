from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from databases.database import Base


class ProductHeight(Base):
    """
    Модель высот продукта

    ## Attrs:
      - product_id: int - идентификатор продукта FK Product
      - height_id: int - идентификатор высоты FK Height
    """

    __tablename__ = "product_height"

    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"),
        primary_key=True,
    )
    height_id: Mapped[int] = mapped_column(
        ForeignKey("height.id", ondelete="CASCADE"),
        primary_key=True,
    )


class ProductMemorySize(Base):
    """
    Модель объемов памяти продукта

    ## Attrs:
      - product_id: int - идентификатор продукта FK Product
      - memory_size_id: int - идентификатор объема памяти
        FK MemorySize
    """

    __tablename__ = "product_memory_size"

    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"),
        primary_key=True,
    )
    memory_size_id: Mapped[int] = mapped_column(
        ForeignKey("memory_size.id", ondelete="CASCADE"),
        primary_key=True,
    )


class ProductColor(Base):
    """
    Модель цветов продукта

    ## Attrs:
      - product_id: int - идентификатор продукта FK Product
      - color_id: int - идентификатор цвета
        FK Color
    """

    __tablename__ = "product_color"

    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"),
        primary_key=True,
    )
    color_id: Mapped[int] = mapped_column(
        ForeignKey("color.id", ondelete="CASCADE"),
        primary_key=True,
    )
