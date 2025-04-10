from pydantic import BaseModel

from constants.property import PropertyType


class PropertyBase(BaseModel):
    propetry_type: PropertyType
    value: str
