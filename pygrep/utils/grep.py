from re import Pattern

# Types
from interfaces.arguments import PyGrepArguments
from interfaces.exceptions import PyGrepException

# Utils
from utils.format_printable import format_printable


def grep(pattern: Pattern, path: str, args: PyGrepArguments):
    try:
        line_number = 0

        count = 0
        printables: list[str] = list()

        with open(path, "rb") as file:
            for line in file:
                try:
                    line = line.decode("utf-8")
                except:
                    continue

                match = pattern.search(line)

                if match and not args.invert_match:
                    printables.append(format_printable(pattern, path, line_number, line, args))
                    count += 1

                if not match and args.invert_match:
                    printables.append(format_printable(pattern, path, line_number, line, args))
                    count += 1

                line_number += 1

        if args.count_lines and count:
            print(f"Matches Found: {count}")

        for printable in printables:
            print(printable)

    except Exception as e:
        raise PyGrepException(str(e))
