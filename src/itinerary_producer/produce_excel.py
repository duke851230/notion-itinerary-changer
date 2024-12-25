from __future__ import annotations
from typing import (
    TYPE_CHECKING, List,
)

if TYPE_CHECKING:
    pass

import os
from datetime import datetime
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl import Workbook

from configer import configer
from helpers.excel.sheet import (
    initialize_sheet,
    set_timeline_in_sheet,
    insert_activities_to_sheet,
)
from helpers.excel.utils import (
    get_timeline_data,
)
from helpers.notion.utils import (
    get_daily_activities,
)
from helpers.check_data import (
    check_activities_time,
    check_activities_required_fields,
    check_options_in_activities_data_is_vaild,
)


FILE_PATH: str = os.path.join(
    configer.excel.EXCEL_BASIC_DIR,
    configer.excel.FILE_NAME
)

def produce_schedule_excel(file_path: str) -> None:
    wb: Workbook = Workbook()
    sheet: Worksheet = wb.active

    if configer.excel.SCHEDULE_TIMELINE_INTERVAL % configer.excel.MINIMAL_INTERVAL != 0:
        raise ValueError("SCHEDULE_TIMELINE_INTERVAL 必須是 MINIMAL_INTERVAL 的整數倍")
    row_number_in_one_timeline_interval: int = configer.excel.SCHEDULE_TIMELINE_INTERVAL // configer.excel.MINIMAL_INTERVAL

    initialize_sheet(
        sheet=sheet,
        merge_row_num=row_number_in_one_timeline_interval
    )

    timeline_start_at: List[str] = configer.excel.SCHEDULE_TIMELINE_START_AT.split(":")
    timeline_end_at: List[str] = configer.excel.SCHEDULE_TIMELINE_END_AT.split(":")

    start_timeline, end_timeline = get_timeline_data(
        start_at=datetime(9999, 1, 1, int(timeline_start_at[0]), int(timeline_start_at[1])),
        end_at=datetime(9999, 1, 1, int(timeline_end_at[0]), int(timeline_end_at[1])),
        start_row_number=2,
        time_interval=configer.excel.MINIMAL_INTERVAL
    )
    set_timeline_in_sheet(
        sheet=sheet,
        column="A",
        timeline_data=[start_timeline, end_timeline],
        merge_row_num=row_number_in_one_timeline_interval
    )

    activities: List[list] = get_daily_activities()
    check_activities_time(activities, configer.excel.SCHEDULE_TIMELINE_START_AT, configer.excel.SCHEDULE_TIMELINE_END_AT)
    check_activities_required_fields(activities)
    check_options_in_activities_data_is_vaild(activities)

    insert_activities_to_sheet(
        sheet=sheet,
        activities=activities,
        timeline=end_timeline,
        start_column="B"
    )

    wb.save(file_path)


if __name__ == "__main__":
    produce_schedule_excel(FILE_PATH)
