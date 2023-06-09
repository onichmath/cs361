"""
Author: Matthew O'Malley-Nichols
Description: CLI main flow
"""
import sys
import single_file_operations
import database_operations
import sys_operations
from questions import p_help, start_screen
"""
Refactoring ideas:
    Make each function do only 1 thing. Make functions require more things as params
    Ex: require path as param instead of getting path during function
    get rid of repeated code
    comment each function
"""

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
        sys_operations.sys_print_hash()
