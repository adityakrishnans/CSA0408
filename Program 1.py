import os
import subprocess

def main():
    # Current process ID
    current_pid = os.getpid()
    print(f"Current Process ID: {current_pid}")

    # Parent process ID using os.getppid()
    parent_pid = os.getppid()
    print(f"Parent Process ID: {parent_pid}")

    # Create a new process (opens Notepad in Windows)
    print("\nCreating a new process (Notepad)...")
    new_process = subprocess.Popen(["notepad.exe"])

    print(f"New Process ID (Child): {new_process.pid}")

if __name__ == "__main__":
    main()


