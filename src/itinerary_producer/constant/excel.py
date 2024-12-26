from __future__ import annotations

from typing import TYPE_CHECKING, Dict

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


class ActivityType(Enum):
    RESTAURANT = "餐廳"
    SNACK = "點心"
    ACCOMMODATION = "住宿"
    ATTRACTION = "景點"
    TRANSPORTATION = "交通"
    PACKAGE_TOUR = "套裝行程"
    ERRANDS = "雜務"
    OTHERS = "其他"


# ACTIVITY_DISPLAY_TEXT_WITH_TYPE_MAPPING 與 BACKGROUND_COLOR_WITH_TYPE_MAPPING 需要一一對應
ACTIVITY_DISPLAY_TEXT_WITH_TYPE_MAPPING: Dict[str, str] = {
    ActivityType.RESTAURANT.value: "{activity_name}\n{start_time}~{end_time}",
    ActivityType.SNACK.value: "{activity_name}\n{start_time}~{end_time}",
    ActivityType.ACCOMMODATION.value: "{activity_name}\n{start_time}~{end_time}",
    ActivityType.ATTRACTION.value: "{activity_name}\n{start_time}~{end_time}",
    ActivityType.TRANSPORTATION.value: "{activity_name}\n{start_time}~{end_time}",
    ActivityType.PACKAGE_TOUR.value: "{activity_name}\n{start_time}~{end_time}",
    ActivityType.ERRANDS.value: "{activity_name}({start_time}~{end_time})",
    ActivityType.OTHERS.value: "{activity_name}({start_time}~{end_time})",
}

BACKGROUND_COLOR_WITH_TYPE_MAPPING: Dict[str, str] = {
    ActivityType.RESTAURANT.value: ColorMap.blue.value,
    ActivityType.ATTRACTION.value: ColorMap.green.value,
    ActivityType.TRANSPORTATION.value: ColorMap.orange.value,
    ActivityType.ERRANDS.value: ColorMap.gray.value,
    ActivityType.PACKAGE_TOUR.value: ColorMap.purple.value,
    ActivityType.SNACK.value: ColorMap.pink.value,
    ActivityType.ACCOMMODATION.value: ColorMap.yellow.value,
    ActivityType.OTHERS.value: ColorMap.beige.value,
}
