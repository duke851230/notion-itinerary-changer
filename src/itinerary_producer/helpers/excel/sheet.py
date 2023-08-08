from __future__ import annotations
from typing import (
    TYPE_CHECKING, List, Optional
)

if TYPE_CHECKING:
    from openpyxl.cell.cell import Cell

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

def set_timeline_in_sheet(sheet: Worksheet, column: str, name: str, name_row_number: int, timeline_data: dict) -> None:
    sheet.column_dimensions[column].width = 10
    
    header_cell: Cell = sheet.cell(
        row = name_row_number, 
        column = column_index_from_string(column),
        value = name
    )
    set_general_format_of_cell(header_cell, font_size=11, fill_color=ColorMap.dark_gray.value)

    for val, row_id in timeline_data.items():
        c: Cell = sheet.cell(
            row = row_id, 
            column = column_index_from_string(column),
            value = val
        )
        set_general_format_of_cell(c, font_size=13, fill_color=ColorMap.gray.value)
    
def insert_activities_to_sheet(
    sheet: Worksheet,
    activities: List[list],
    timeline: dict,
    start_column: str
) -> None:
    """ Insert activities to excel.

    :param sheet: current work sheet object
    :param activities: everyday activities
    :param timeline: schedule's end timeline which is used to merge activity's cell
    :param start_column: define where to start writing

    :return: None
    """
    current_column: str = start_column

    for today_activities in activities:
        date_cell: Cell = sheet.cell(
            row=1,
            column=column_index_from_string(current_column),
            value=today_activities[0]["start_at"][:10]
        )
        set_general_format_of_cell(date_cell, font_size=15, fill_color=ColorMap.purple.value)

        header_cell: Cell = sheet.cell(
            row=2,
            column=column_index_from_string(current_column),
            value=today_activities[0]["day"]
        )
        set_general_format_of_cell(header_cell, font_size=18, fill_color=ColorMap.dark_gray.value)

        for activity in today_activities:
            start_time_str: str = get_hour_minute_time(activity["start_at"])
            end_time_str: str = get_hour_minute_time(activity["end_at"])
            start_row_index: int = timeline[start_time_str] + 1
            end_row_index: int = timeline[end_time_str]

            sheet.merge_cells(f"{current_column}{start_row_index}:{current_column}{end_row_index}")

            activity_cell: Cell = sheet.cell(
                row=start_row_index,
                column=column_index_from_string(current_column),
                value=f'項目：{activity["name"]}\n位置：{activity["place"]}'
            )
            set_general_format_of_cell(activity_cell, font_size=12, fill_color=get_type_color(activity["type"]))

        current_column = find_next_column_letter(current_column)

def set_general_format_of_cell(cell: Cell, font_size: int, fill_color: Optional[str]) -> None:
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.font = Font(size=font_size)
    if fill_color:
        cell.fill = PatternFill("solid", fgColor=fill_color)
    cell.border = get_default_border()
