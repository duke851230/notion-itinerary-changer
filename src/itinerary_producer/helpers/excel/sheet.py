from __future__ import annotations
from typing import (
    TYPE_CHECKING, List, Optional, Tuple
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
from helpers.general import (
    exchange_place_with_key_and_value,
)
from constant.excel import ColorMap


def initialize_sheet(sheet: Worksheet) -> None:
    sheet.sheet_format.defaultColWidth = 20
    sheet.sheet_format.defaultRowHeight = 35

def set_timeline_in_sheet(sheet: Worksheet, column: str, timeline_data: Tuple[dict]) -> None:
    sheet.column_dimensions[column].width = 14
    
    start_timeline, end_timeline = timeline_data
    start_timeline = exchange_place_with_key_and_value(start_timeline)
    end_timeline = exchange_place_with_key_and_value(end_timeline)

    for row_id, end_time in end_timeline.items():
        c: Cell = sheet.cell(
            row = row_id,
            column = column_index_from_string(column),
            value = f"{start_timeline[row_id]}~{end_time}"
        )
        set_general_format_of_cell(c, font_size=12, fill_color=ColorMap.gray.value)
    
def insert_activities_to_sheet(
    sheet: Worksheet,
    activities: List[list],
    timeline: dict,
    start_column: str
) -> None:
    """ Insert activities and date title to excel.

    :param sheet: current work sheet object
    :param activities: everyday activities
    :param timeline: schedule's end timeline which is used to merge activity's cell
    :param start_column: define where to start writing

    :return: None
    """
    current_column: str = start_column

    for today_activities in activities:
        header_cell: Cell = sheet.cell(
            row=1,
            column=column_index_from_string(current_column),
            value=today_activities[0]["date"]
        )
        set_general_format_of_cell(header_cell, font_size=16, fill_color=ColorMap.dark_gray.value)

        for activity in today_activities:
            start_time_str: str = activity["start_at"]
            end_time_str: str =activity["end_at"]
            start_row_index: int = timeline[start_time_str] + 1
            end_row_index: int = timeline[end_time_str]

            sheet.merge_cells(f"{current_column}{start_row_index}:{current_column}{end_row_index}")

            activity_cell: Cell = sheet.cell(
                row=start_row_index,
                column=column_index_from_string(current_column),
                value=f'{activity["name"]}\n{start_time_str}~{end_time_str}\n位置：{activity["place"]}'
            )
            set_general_format_of_cell(activity_cell, font_size=12, fill_color=get_type_color(activity["type"]))

        current_column = find_next_column_letter(current_column)

def set_general_format_of_cell(cell: Cell, font_size: int, fill_color: Optional[str]) -> None:
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.font = Font(name=u'微軟雅黑', size=font_size)
    if fill_color:
        cell.fill = PatternFill("solid", fgColor=fill_color)
    cell.border = get_default_border()
