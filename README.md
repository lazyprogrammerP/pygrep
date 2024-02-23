# PyGrep

**pygrep** is a Python tool designed to offer functionality similar to the grep command, providing a flexible and efficient way to search for patterns within files.

## Getting Started

To use pygrep, you need to clone the repository to your local machine. Follow these steps:

1. Clone the pygrep repository from GitHub:

```bash
git clone https://github.com/your-username/pygrep.git
```

2. Navigate to the pygrep directory:

```bash
cd pygrep
```

## Usage

### Command Line Interface

pygrep is executed via the command line, accepting a variety of arguments to tailor the search according to your needs.

```bash
python pygrep.py <pattern> <paths> [options]
```

- \<pattern\>: The pattern to search for within the specified files or directories.
- \<paths\>: One or more paths to the files or directories where the search will be conducted.

### Options

| Option                  | Description                                                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-i`, `--ignore-case`   | Perform a case-insensitive search.                                                                                                                  |
| `-n`, `--line-number`   | Display the line number of each match.                                                                                                              |
| `-c`, `--count-lines`   | Display the total count of matches.                                                                                                                 |
| `-l`, `--show-filename` | Display the filename for each match.                                                                                                                |
| `-r`, `--recursive`     | Perform a recursive search in directories.                                                                                                          |
| `-e`, `--invert-match`  | Invert the match to find non-matching lines.                                                                                                        |
| `-w`, `--word-regexp`   | Search for whole words only.                                                                                                                        |
| `-C`, `--color <Color>` | Select the color for highlighting the matched text. Choose from the following RGB color options: <br>`Color.RED` <br>`Color.GREEN` <br>`Color.BLUE` |

### Examples

Search for a specific pattern in a single file:

```bash
python pygrep.py "pattern" file.txt
```

Search for a pattern in multiple files, displaying line numbers:

```bash
python pygrep.py "pattern" file1.txt file2.txt -n
```

Perform a case-insensitive search in a directory:

```bash
python pygrep.py "pattern" directory/ -i
```

Recursively search directories for a pattern, displaying filenames:

```bash
python pygrep.py "pattern" directory/ -r -l
```

# Contributing

Contributions to pygrep are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

Note: pygrep is inspired by the grep command-line tool but offers additional features and flexibility using Python.
