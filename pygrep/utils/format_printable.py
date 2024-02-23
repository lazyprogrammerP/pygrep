import os
import re

# Types
from interfaces.arguments import PyGrepArguments

# Utils
from utils.colorize_match import colorize_match


def format_printable(pattern: re.Pattern, path: str, line_number: int, line: str, args: PyGrepArguments):
    printable = ""

    if args.show_filename:
        printable += f"[{os.path.basename(path)}]: "

    if args.line_number:
        printable += f"[Line {line_number}]: "

    printable += colorize_match(pattern, line.strip(), args.color)

    return printable
