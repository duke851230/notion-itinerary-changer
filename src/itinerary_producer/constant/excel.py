from __future__ import annotations
from typing import (
    TYPE_CHECKING, Dict,
)

if TYPE_CHECKING:
    pass

from enum import Enum


class ColorMap(Enum):
    blue = "00CCFFFF"
    yellow = "00FFFF99"
    beige = "00FFFFCC"
    purple = "00CCCCFF"
    green = "00CCFFCC"
    orange = "00FFCC99"
    pink = "00FF99CC"
    gray = "DDDDDD"
    dark_gray = "00969696"
    white = "00FFFFFF"

# ACTIVITY_DISPLAY_TEXT_WITH_TYPE_MAPPING 與 BACKGROUND_COLOR_WITH_TYPE_MAPPING 需要一一對應
ACTIVITY_DISPLAY_TEXT_WITH_TYPE_MAPPING: Dict[str, str] = {
    "餐廳": "{activity_name}\n{start_time}~{end_time}",
    "點心": "{activity_name}\n{start_time}~{end_time}",
    "住宿": "{activity_name}\n{start_time}~{end_time}",
    "景點": "{activity_name}\n{start_time}~{end_time}",
    "交通": "{activity_name}\n{start_time}~{end_time}",
    "套裝行程": "{activity_name}\n{start_time}~{end_time}",
    "雜務": "{activity_name}({start_time}~{end_time})",
    "其他": "{activity_name}({start_time}~{end_time})"
}

BACKGROUND_COLOR_WITH_TYPE_MAPPING: Dict[str, str] = {
    "餐廳": ColorMap.blue.value,
    "景點": ColorMap.green.value,
    "交通": ColorMap.orange.value,
    "雜務": ColorMap.gray.value,
    "套裝行程": ColorMap.purple.value,
    "點心": ColorMap.pink.value,
    "住宿": ColorMap.yellow.value,
    "其他": ColorMap.beige.value
}
