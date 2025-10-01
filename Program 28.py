import re
import os

def grep(pattern, filename):
    """Simulate grep: search for pattern in a file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found!")
        return

    regex = re.compile(pattern)
    with open(filename, "r") as f:
        for line_no, line in enumerate(f, start=1):
            if regex.search(line):
                print(f"{filename}:{line_no}: {line.strip()}")

if __name__ == "__main__":
    pattern = input("Enter search pattern: ")
    filename = input("Enter filename: ")
    grep(pattern, filename)
