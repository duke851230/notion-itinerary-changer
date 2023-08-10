from __future__ import annotations
from typing import (
    TYPE_CHECKING, List,
)

if TYPE_CHECKING:
    pass


def get_title(property_info: dict) -> str:
    inner_info: dict = property_info["title"][0]
    return inner_info["text"]["content"]

def get_rich_text(property_info: dict) -> str:
    inner_info_list: List[dict] = property_info["rich_text"]
    if len(inner_info_list) == 0:
        return ""
    
    return inner_info_list[0]["text"]["content"]

def get_date(property_info: dict) -> str:
    return property_info["date"]["start"]

def get_select(property_info: dict) -> str:
    if property_info.get("select") is None:
        return ""
    
    return property_info["select"]["name"]
