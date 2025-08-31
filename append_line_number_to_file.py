import sys
from pathlib import Path

def print_file_with_line_numbers(filepath, start=None, end=None, output_file=None):
    """
    Print file contents with line numbers and optionally save to a file.

    Args:
        filepath (str): Path to the file.
        start (int): Optional. Start line number (1-based).
        end (int): Optional. End line number (inclusive).
        output_file (str): Optional. Path to save the output.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        return

    lines = []
    with filepath.open("r") as f:
        for idx, line in enumerate(f, start=1):
            if start and idx < start:
                continue
            if end and idx > end:
                break
            lines.append(f"{idx:4}: {line.rstrip()}")

    # Print to console
    for l in lines:
        print(l)

    # Save to file if requested
    if output_file:
        with open(output_file, "w") as out:
            out.write("\n".join(lines))
        print(f"\n✅ Output written to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python view_lines.py <filepath> [start] [end] [output_file]")
        sys.exit(1)

    filepath = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else None
    end = int(sys.argv[3]) if len(sys.argv) > 3 else None
    output_file = sys.argv[4] if len(sys.argv) > 4 else None

    print_file_with_line_numbers(filepath, start, end, output_file)
