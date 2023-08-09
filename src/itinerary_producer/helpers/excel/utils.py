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


def get_timeline_data(
    start_at: datetime,
    end_at: datetime,
    start_row_number,
    time_interval: int
) -> Tuple[Dict[str, int], Dict[str, int]]:
    """ Get schedule start and end timeline.

    :param start_at: timeline start time
    :param end_at: timeline end time
    :param start_row_number: it be used to calculate every moment's row id
    :param time_interval: timeline interval
    
    :return: (start timeline, end timeline)

    :return example:
    (
        # start timeline
        {
            '07:30': 3,
            '08:00': 4,
            '08:30': 5,
            'moment': row_id, ...
        },
        # end timeline
        {...}
    )
    """
    start_timeline: Dict[str, int] = {}
    end_timeline: Dict[str, int] = {}
    current_row: int = start_row_number
    current_datetime: datetime = start_at

    while current_datetime <= end_at:
        start_time_str: str = current_datetime.strftime("%H:%M")
        start_timeline[start_time_str] = current_row
        
        end_time: datetime = current_datetime + timedelta(minutes=time_interval)
        end_time_str: str = end_time.strftime("%H:%M")
        end_timeline[end_time_str] = current_row

        current_row += 1
        current_datetime = current_datetime + timedelta(minutes=time_interval)

    return (start_timeline, end_timeline)

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

