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
    get_type_color,
    get_default_border,
    get_hour_minute_time,
)
from constant.excel import ColorMap


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
        c.fill = PatternFill("solid", fgColor=ColorMap.gray.value)
        c.border = get_default_border()
    
def insert_activities_to_sheet(
        sheet: Worksheet,
        activities: List[list],
        timeline: dict,
        start_column: str="B"
    ) -> None:

    current_column: str = start_column

    for today_activities in activities:
        date_cell = sheet.cell(
            row=1,
            column=column_index_from_string(current_column),
            value=today_activities[0]["start_at"][:10]
        )
        date_cell.alignment = Alignment(horizontal="center", vertical="center")
        date_cell.font = Font(size=15)
        date_cell.fill = PatternFill("solid", fgColor=ColorMap.purple.value)
        date_cell.border = get_default_border()

        header_cell = sheet.cell(
            row=2,
            column=column_index_from_string(current_column),
            value=today_activities[0]["day"]
        )
        header_cell.alignment = Alignment(horizontal="center", vertical="center")
        header_cell.font = Font(size=18)
        header_cell.fill = PatternFill("solid", fgColor=ColorMap.gray.value)
        header_cell.border = get_default_border()

        for activity in today_activities:
            start_row_index: int = timeline[
                get_hour_minute_time(activity["start_at"])
            ] + 1
            end_row_index: int = timeline[
                get_hour_minute_time(activity["end_at"])
            ]
            sheet.merge_cells(f"{current_column}{start_row_index}:{current_column}{end_row_index}")

            activity_cell = sheet.cell(
                row=start_row_index,
                column=column_index_from_string(current_column),
                value=f'項目：{activity["name"]}\n位置：{activity["place"]}'
            )
            activity_cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            activity_cell.font = Font(size=14)
            activity_cell.fill = PatternFill(
                "solid", fgColor=get_type_color(activity["type"])
            )
            activity_cell.border = get_default_border()

        current_column = find_next_column_letter(current_column)


