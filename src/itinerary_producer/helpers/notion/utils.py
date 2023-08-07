from __future__ import annotations
from typing import (
    TYPE_CHECKING, Callable, Dict,
)

if TYPE_CHECKING:
    pass

from configer import configer
from constant.notion import PropertyType
from helpers.notion import property
from helpers.notion.api import (
    get_databases_data,
)


def get_daily_card_info() -> dict:
    data = get_databases_data(configer.notion.DATABASE_ID)

    notion_data: dict = {}
    for card in data["results"]:
        properties: Dict[str, dict] = card["properties"]

        card_info: dict = {}
        for field, info in properties.items():
            lower_field: str = field.lower()
            if lower_field in PropertyType.__members__:
                property_type: str = PropertyType[lower_field].value
                method: Callable = getattr(property, f"get_{property_type}")
                card_info[lower_field] = method(info)
        
        day: str = card_info[PropertyType.day.name]
        if day not in notion_data:
            notion_data[day] = []
        
        notion_data[day].append(card_info)

    print(notion_data)
    return notion_data