"""
Author: Matthew O'Malley-Nichols
Description: CLI main flow
"""
import sys
import single_file_operations
import database_operations
from questions import p_help, start_screen
"""
Refactoring ideas:
    put each "line" of questions and functions into their own file
    try to improve composition by changing around file
    get rid of repeated code
    comment each function
"""

def sys_print_hash():
    path = sys.argv[1]
    file_name = get_filename_from_path(path)
    try:
        blake_hash = get_single_file_hash(path)
    except:
        p_help()
        raise FileNotFoundError
    print(f"The hash of {file_name} is:\n{blake_hash.hexdigest()}")

def main():
    """
    Opens up cli if not given a file hash
    """
    if len(sys.argv) == 1:
        while True:
            init_answer = start_screen()
            if init_answer == "Help":
                p_help()
                continue
            if init_answer == "Single File Operations":
                path,hash = single_file_operations.get_single_file_path_hash()
                if path:
                    single_file_operations.single_file_operations(path,hash)
                continue
            if init_answer == "Database Operations":
                database_operations.database_operations()
                continue
            if init_answer == "Exit":
                break
            continue
    # Make sure this case doesn
    else:
        sys_print_hash()
