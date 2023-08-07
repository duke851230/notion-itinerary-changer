from __future__ import annotations
from typing import (
    TYPE_CHECKING, Dict,
)

if TYPE_CHECKING:
    pass

from datetime import datetime, timedelta
from openpyxl.utils import (
    get_column_letter,
    column_index_from_string,
)


def get_timeline_data(start_at: datetime, end_at: datetime, start_row_number: int, time_interval: int=30) -> Dict[str, int]:
    timeline: Dict[str, int] = {}
    current_id: int = start_row_number

    while start_at <= end_at:
        time_str: str = start_at.strftime("%H:%M")
        timeline[time_str] = current_id

        current_id += 1
        start_at = start_at + timedelta(minutes=time_interval)
    
    return timeline

def find_next_column_letter(current_column_letter: str) -> str:
    next_column_id: int = column_index_from_string(current_column_letter) + 1
    next_column_letter: str = get_column_letter(next_column_id)

    return next_column_letter