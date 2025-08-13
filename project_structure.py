"""
Project Structure Generator with Line Counts

This script generates a tree-like representation of a project's directory structure,
skipping unnecessary files and directories such as `.git`, `__pycache__`, `.pyc` files, etc.
It displays each file along with:
    - For Python files (.py): The number of lines in the file
    - For other files: The file size in KB

The output is:
    1. Printed to the console
    2. Saved to a text file named 'project_structure.txt'

Features:
---------
- Recursively traverses the given root directory.
- Skips predefined directories (e.g., `.git`, `node_modules`, `__pycache__`) and file extensions.
- Provides a clean, human-readable tree structure with Unicode branch characters.
- Includes line count for `.py` files and size in KB for other files.
- Handles file reading errors gracefully without stopping the script.

Configuration:
--------------
- `SKIP_DIRS`: Set of directory names to exclude from the output.
- `SKIP_EXTS`: Set of file extensions to exclude from the output.
- `OUTPUT_FILE`: Name of the file where the tree output will be stored.

Usage:
------
1. Place this script at the root of the project you want to analyze.
2. (Optional) Modify `root_directory` in the `__main__` section to point to a different folder.
3. Run the script:
       python project_structure.py

Example Output:
---------------
Project structure for: /path/to/project

├── app/
│   ├── __init__.py (0 lines)
│   ├── models/
│   │   ├── user.py (120 lines)
│   │   └── book.py (95 lines)
│   └── routes/
│       └── main.py (40 lines)
├── requirements.txt (1 KB)
└── main.py (15 lines)

Author:
-------
Vikram Vivek AI Dev - Generated with the assistance of ChatGPT 
"""

import os

# Configuration — add any patterns you want to skip
SKIP_DIRS = {'.git', '__pycache__', '.idea', '.vscode', '.mypy_cache', '.pytest_cache', 'node_modules'}
SKIP_EXTS = {'.pyc', '.pyo', '.log', '.tmp'}

OUTPUT_FILE = "project_structure.txt"


def get_file_info(file_path):
    """Return line count for Python files or size for others."""
    try:
        if file_path.endswith(".py"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = sum(1 for _ in f)
            return f"({lines} lines)"
        else:
            size_kb = os.path.getsize(file_path) // 1024
            return f"({size_kb} KB)"
    except Exception:
        return "(error reading file)"


def print_tree(root_dir, prefix="", output_lines=None):
    entries = sorted(os.listdir(root_dir))
    entries = [e for e in entries if e not in SKIP_DIRS and not any(e.endswith(ext) for ext in SKIP_EXTS)]

    for index, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        connector = "└── " if index == len(entries) - 1 else "├── "

        if os.path.isdir(path):
            line = f"{prefix}{connector}{entry}/"
            print(line)
            output_lines.append(line)
            extension = "    " if index == len(entries) - 1 else "│   "
            print_tree(path, prefix + extension, output_lines)
        else:
            info = get_file_info(path)
            line = f"{prefix}{connector}{entry} {info}"
            print(line)
            output_lines.append(line)


if __name__ == "__main__":
    root_directory = "."  # Change if needed
    output_lines = []
    header = f"Project structure for: {os.path.abspath(root_directory)}\n"
    print(header)
    output_lines.append(header.strip())

    print_tree(root_directory, output_lines=output_lines)

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"\nSaved structure to '{OUTPUT_FILE}'")
