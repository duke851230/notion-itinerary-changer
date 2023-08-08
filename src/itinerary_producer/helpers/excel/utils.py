from __future__ import annotations
from typing import (
    TYPE_CHECKING, Dict, Tuple
)

if TYPE_CHECKING:
    pass

from datetime import datetime, timedelta
from openpyxl.utils import (
    get_column_letter,
    column_index_from_string,
)
from openpyxl.styles import (
    Border, Side,
)

from constant.excel import ColorMap


def get_timeline_data(start_at: datetime, end_at: datetime, time_interval: int=30) -> Tuple[Dict[str, int], Dict[str, int]]:
    pre_timline: Dict[str, int] = {}
    timeline: Dict[str, int] = {}
    current_id: int = 0

    while start_at <= end_at:
        pre_time: datetime = start_at - timedelta(minutes=time_interval)
        pre_time_str: str = pre_time.strftime("%H:%M")
        pre_timline[pre_time_str] = current_id

        time_str: str = start_at.strftime("%H:%M")
        timeline[time_str] = current_id

        current_id += 1
        start_at = start_at + timedelta(minutes=time_interval)
    
    return (pre_timline, timeline)

def find_next_column_letter(current_column_letter: str) -> str:
    next_column_id: int = column_index_from_string(current_column_letter) + 1
    next_column_letter: str = get_column_letter(next_column_id)

    return next_column_letter

def get_type_color(type_name: str) -> str:
    mapping: dict = {
        "餐廳": ColorMap.blue.value,
        "景點": ColorMap.green.value,
        "交通": ColorMap.orange.value
    }

    if type_name not in mapping:
        return ColorMap.beige.value
    
    return mapping[type_name]

def get_default_border() -> Border:
    return Border(
        bottom=Side(style='thin'),
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
    )

def get_hour_minute_time(datetime_str: str) -> str:
    datetime_obj: datetime = datetime.fromisoformat(datetime_str)
    return datetime_obj.strftime("%H:%M")
