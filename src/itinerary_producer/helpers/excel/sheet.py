from __future__ import annotations
from typing import (
    TYPE_CHECKING, List,
)

if TYPE_CHECKING:
    pass

from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.utils import column_index_from_string
from openpyxl.styles import (
    Alignment, Font, PatternFill, Border, Side,
)

from helpers.excel.utils import (
    find_next_column_letter,
    get_timeline_data,
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
    
def insert_activities_to_sheet(
        sheet: Worksheet,
        activities: List[list],
        timeline: dict,
        start_column: str="B"
    ) -> None:

    current_column: str = start_column

    for today_activities in activities:
        header_cell = sheet.cell(
            row=1,
            column=column_index_from_string(current_column),
            value=today_activities[0]["day"]
        )
        header_cell.alignment = Alignment(horizontal="center", vertical="center")
        header_cell.font = Font(size=18)

        for activity in today_activities:
            start_row_index: int = timeline[activity["start_at"]]
            end_row_index: int = timeline[activity["end_at"]]
            sheet.merge_cells(f"{current_column}{start_row_index}:{current_column}{end_row_index}")

            activity_cell = sheet.cell(
                row=start_row_index,
                column=column_index_from_string(current_column),
                value=activity["name"]
            )
            activity_cell.alignment = Alignment(horizontal="center", vertical="center")
            activity_cell.font = Font(size=14)

        current_column = find_next_column_letter(current_column)


