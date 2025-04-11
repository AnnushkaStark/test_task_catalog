from constants.property import PropertyType


async def get_property_type() -> dict[str, str]:
    return {
        property_type.name: property_type.value
        for property_type in PropertyType
    }
