#!/usr/bin/env python3
""" Log parsing"""
import sys
import signal

# Define a dictionary to store status code counts
status_counts = {}

# Initialize total file size
total_file_size = 0


# Define a signal handler to handle keyboard interrupts
def signal_handler(signal, frame):
    """
    signal handler
    """
    print_statistics()
    sys.exit(0)


# Function to print statistics
def print_statistics():
    """
    print sratistic
    """
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


# Register signal handler for keyboard interrupts (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


# Process input line by line from stdin
for line_number, line in enumerate(sys.stdin, start=1):
    try:
        # Split the line into components
        ip_address, _, _, status_code_str, file_size_str = line.split(" ")[0:5]
        # Parse status code and file size
        status_code = int(status_code_str)
        file_size = int(file_size_str)
        # Update total file size
        total_file_size += file_size
        # Update status code count
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1
        # Print statistics after every 10 lines
        if line_number % 10 == 0:
            print_statistics()
    except ValueError:
        # Skip lines that do not match the expected format
        continue

# Print final statistics
print_statistics()
