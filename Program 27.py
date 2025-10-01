import os
import stat
import time

def list_files(path="."):
    try:
        entries = os.scandir(path)
        print(f"\nListing for directory: {os.path.abspath(path)}\n")

        for entry in entries:
            info = entry.stat()

            # File permissions (like rwx)
            permissions = stat.filemode(info.st_mode)

            # File size
            size = info.st_size

            # Last modified time
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info.st_mtime))

            # Print in ls -l style
            print(f"{permissions} {size:8d} {mtime} {entry.name}")

    except FileNotFoundError:
        print(f"Directory '{path}' not found!")
    except PermissionError:
        print(f"Permission denied for '{path}'!")

if __name__ == "__main__":
    path = input("Enter directory path (leave blank for current dir): ").strip()
    if not path:
        path = "."
    list_files(path)
