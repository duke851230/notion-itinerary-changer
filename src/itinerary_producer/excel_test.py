from __future__ import annotations
from typing import (
    TYPE_CHECKING, List, Optional
)

if TYPE_CHECKING:
    pass

import os
from datetime import datetime
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl import Workbook

from configer import configer
from helpers.excel.sheet import (
    set_timeline_in_sheet,
)
from helpers.excel.utils import (
    get_timeline_data,
)


file_path: str = os.path.join(configer.excel.EXCEL_BASIC_DIR, "test.xlsx")

wb: Workbook = Workbook()
sheet: Worksheet = wb.active

timeline: dict = get_timeline_data(
    start_at=datetime(9999, 1, 1, 8, 30),
    end_at=datetime(9999, 1, 1, 20, 00),
    start_row_number=2,
    time_interval=30
)
print(timeline)
set_timeline_in_sheet(sheet, timeline)

wb.save(file_path)
