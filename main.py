import os
import re
from argparse import ArgumentParser
from glob import glob


def display_match(path, line, line_number, flags):
    if flags.show_filename:
        print(f"[{path}]: ", end="")

    if flags.line_number:
        print(f"{line_number}: {line}", end=" ")


def grep_file(pattern, path, args):
    line_number = 0

    try:
        with open(path, "r") as file:
            for line in file:
                line_number += 1
                match = pattern.search(line)

                if match and not args.invert_match:
                    display_match(path, line, line_number, args)

                if not match and args.invert_match:
                    display_match(path, line, line_number, args)
    except Exception as e:
        # print(e)
        pass


def grep(pattern, paths, args):
    for path in paths:
        if os.path.isfile(path):
            grep_file(pattern, path, args)
            pass
        else:
            if os.path.isdir(path):
                if args.recursive:
                    for root, _, file_paths in os.walk(path):
                        for file_path in file_paths:
                            abs_file_path = os.path.join(root, file_path)
                            grep_file(pattern, abs_file_path, args)
                else:
                    raise Exception(f"pygrep: {path}: is a directory")
            else:
                raise Exception(f"pygrep: {path}: no such file or directory")


def main():
    cli_parser = ArgumentParser(description="pygrep: a grep-like tool built using python")

    # defining the positional arguments
    cli_parser.add_argument("pattern", help="the pattern to search for")
    cli_parser.add_argument("paths", nargs="+", help="the paths to search in")

    # defining the optional arguments
    cli_parser.add_argument("-i", "--ignore-case", action="store_true", help="perform case insensitive search")
    cli_parser.add_argument("-n", "--line-number", action="store_true", help="display the line number of the match")
    cli_parser.add_argument("-c", "--count-lines", action="store_true", help="display the count of matched lines")
    cli_parser.add_argument("-l", "--show-filename", action="store_true", help="display the file name of matched lines")
    cli_parser.add_argument("-r", "--recursive", action="store_true", help="perform recursive search in a directory")
    cli_parser.add_argument("-e", "--invert-match", action="store_true", help="perform an inverted search")
    cli_parser.add_argument("-w", "--word-regexp", action="store_true", help="perform a search on whole word")

    args = cli_parser.parse_args()
    pattern = args.pattern

    if args.ignore_case:
        pattern = re.compile(args.pattern, re.IGNORECASE)
    else:
        pattern = re.compile(args.pattern)

    if args.word_regexp:
        pattern = re.compile(f"\b{pattern}\b")

    # check for wildcard patterns
    extended_paths = []
    for path in args.paths:
        if ("*" in path) or ("?" in path):
            extended_paths.extend(glob(path))
        else:
            extended_paths.append(path)

    grep(pattern, extended_paths, args)
