from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from constant.notion import PropertyType


def get_title(property_info: dict) -> str:
    inner_info: dict = property_info["title"][0]
    return inner_info["text"]["content"]

def get_rich_text(property_info: dict) -> str:
    inner_info: dict = property_info["rich_text"][0]
    return inner_info["text"]["content"]

def get_date(property_info: dict) -> str:
    return property_info["date"]["start"]



