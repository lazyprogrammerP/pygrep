from dataclasses import dataclass
from typing import Optional

# Enums
from enums.color import Color


@dataclass
class PyGrepArguments:
    pattern: str
    paths: str
    ignore_case: Optional[bool] = False
    line_number: Optional[bool] = False
    count_lines: Optional[bool] = False
    show_filename: Optional[bool] = False
    recursive: Optional[bool] = False
    invert_match: Optional[bool] = False
    word_regexp: Optional[bool] = False
    color: Optional[Color] = None
