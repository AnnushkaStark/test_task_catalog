from constants.crud_types import CreateSchemaType, ModelType

from .crud_mixins.base import BaseCRUD
from .crud_mixins.create import CreateAsync
from .crud_mixins.delete import DeleteAsync
from .crud_mixins.read import ReadAsync


class BaseAsyncCRUD(
    BaseCRUD[ModelType],
    CreateAsync[ModelType, CreateSchemaType],
    ReadAsync[ModelType],
    DeleteAsync[ModelType],
):
    """
    CRUD object with default methods to Create, Read, Update, Delete (CRUD)
    **Parameters**
    * `model`: A SQLAlchemy model class
    * `schema`: A Pydantic model (schema) class
    """

    ...
