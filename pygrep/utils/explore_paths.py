import os

from interfaces.arguments import PyGrepArguments
from interfaces.exceptions import DirectoryWithoutRecursive, NotAFileOrDirectory, RecursiveWithoutDirectory


def explore_paths(paths: list[str], args: PyGrepArguments) -> list[str]:
    flattened_paths: list[str] = list()

    for path in paths:
        if os.path.isfile(path):
            flattened_paths.append(path)
        else:
            if os.path.isdir(path):
                if args.recursive:
                    # recursively crawl the directory and pattern match in the files in the directory
                    for root, _, directory_file_paths in os.walk(path):
                        for directory_file_path in directory_file_paths:
                            flattened_paths.append(os.path.join(root, directory_file_path))
                else:
                    raise DirectoryWithoutRecursive(path)
            else:
                raise NotAFileOrDirectory(path)

    return flattened_paths
