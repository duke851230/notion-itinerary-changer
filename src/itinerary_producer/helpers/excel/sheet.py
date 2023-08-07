from __future__ import annotations
from typing import (
    TYPE_CHECKING, 
)

if TYPE_CHECKING:
    pass

from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.utils import column_index_from_string
from openpyxl.styles import (
    Alignment, PatternFill, Border, Side,
)


def initialize_sheet(sheet: Worksheet) -> None:
    sheet.sheet_format.defaultColWidth = 20
    sheet.sheet_format.defaultRowHeight = 35
    sheet.column_dimensions["A"].width = 10

def set_timeline_in_sheet(sheet: Worksheet, timeline_data: dict) -> None:
    for val, row_id in timeline_data.items():
        c = sheet.cell(
            row = row_id, 
            column = column_index_from_string("A"),
            value = val
        )
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)  # wrap_text=True 自動換行
