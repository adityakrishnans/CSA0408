import os

def copy_file(source, destination):
    # Open source file for reading (O_RDONLY)
    src_fd = os.open(source, os.O_RDONLY)
    
    # Open destination file for writing (create if not exists, truncate if exists)
    dst_fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

    while True:
        # Read 1024 bytes at a time
        data = os.read(src_fd, 1024)
        if not data:  # EOF
            break
        os.write(dst_fd, data)

    # Close file descriptors
    os.close(src_fd)
    os.close(dst_fd)
    print(f"Copied content from '{source}' to '{destination}'")

# Example usage
if __name__ == "__main__":
    copy_file("source.txt", "destination.txt")





