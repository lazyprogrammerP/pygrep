import re
from argparse import ArgumentParser
from glob import glob

# Enums
from enums.color import Color

# Types
from interfaces.arguments import PyGrepArguments

# Utils
from utils.explore_paths import explore_paths
from utils.grep import grep

argparser = ArgumentParser(description="pygrep: a grep-like tool built using python")

# defining positional arguments
argparser.add_argument("pattern", help="The pattern to search for.")
argparser.add_argument("paths", nargs="+", help="The paths to search for the pattern in.")

# defining optional arguments
argparser.add_argument("-i", "--ignore-case", action="store_true", help="Perform a case-insensitive search.")
argparser.add_argument("-n", "--line-number", action="store_true", help="Display the line number of each match.")
argparser.add_argument("-c", "--count-lines", action="store_true", help="Display the total count of matches.")
argparser.add_argument("-l", "--show-filename", action="store_true", help="Display the filename for each match.")
argparser.add_argument("-r", "--recursive", action="store_true", help="Perform a recursive search in directories.")
argparser.add_argument("-e", "--invert-match", action="store_true", help="Invert the match to find non-matching lines.")
argparser.add_argument("-w", "--word-regexp", action="store_true", help="Search for whole words only.")
argparser.add_argument("-C", "--color", type=Color, choices=list(Color), help="Select the color for highlighting the matched text.")

args = PyGrepArguments(**vars(argparser.parse_args()))


# building pattern to match
pattern = re.compile(args.pattern)

if args.ignore_case:
    pattern = re.compile(args.pattern, re.IGNORECASE)

if args.word_regexp:
    pattern = re.compile(f"\\b{args.pattern}\\b")  # \b: word boundary expression


# extend support for wildcard files
extended_paths: list[str] = list()
for path in args.paths:
    if ("*" in path) or ("?" in path):
        extended_paths.extend(glob(path))
    else:
        extended_paths.append(path)

traceable_paths = explore_paths(extended_paths, args)

for traceable_path in traceable_paths:
    grep(pattern, traceable_path, args)
