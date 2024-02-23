class PyGrepException(Exception):
    def __init__(self, message: str):
        super().__init__(f"[pygrep]: {message}")


class RecursiveWithoutDirectory(PyGrepException):
    def __init__(self, path: str):
        super().__init__(f"{path}: is not a directory. recursion (-r) can only be used to search in directories.")


class DirectoryWithoutRecursive(PyGrepException):
    def __init__(self, path: str):
        super().__init__(f"{path}: is a directory. use the recursion (-r) option to search in directories.")


class NotAFileOrDirectory(PyGrepException):
    def __init__(self, path: str):
        super().__init__(f"{path}: is not a file or directory.")
