import os
import stat

def demo_fcntl(filename):
    """Simulate fcntl (file locking) for Windows."""
    print(f"Simulated fcntl: Locking file '{filename}' (not supported on Windows).")

def demo_seek(filename):
    """Simulate lseek: move file pointer."""
    with open(filename, "r") as f:
        f.seek(5)  # Move pointer to 5th byte
        data = f.read(10)
        print(f"After seek(5), next 10 bytes: '{data}'")

def demo_stat(filename):
    """Show file status using os.stat()."""
    st = os.stat(filename)
    print(f"\nFile Stats for {filename}:")
    print(f"Size: {st.st_size} bytes")
    print(f"Permissions: {oct(st.st_mode)}")
    print(f"Last Modified: {st.st_mtime}")

def demo_opendir_readdir(path):
    """Simulate opendir & readdir using os.scandir()."""
    print(f"\nContents of directory '{path}':")
    with os.scandir(path) as entries:
        for entry in entries:
            type_info = "Directory" if entry.is_dir() else "File"
            print(f"- {entry.name} ({type_info})")

if __name__ == "__main__":
    # Create sample file
    filename = "sample.txt"
    with open(filename, "w") as f:
        f.write("Hello World! This is a demo file for system calls.\n")

    print("\n--- Simulating UNIX I/O System Calls in Windows ---")

    demo_fcntl(filename)             # Simulated fcntl
    demo_seek(filename)              # File pointer movement
    demo_stat(filename)              # File metadata
    demo_opendir_readdir(".")        # List current directory
