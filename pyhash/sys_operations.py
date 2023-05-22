"""
Author: Matthew O'Malley-Nichols
Description: Print file hash from sys argument. Called from cli
"""
import sys
from questions import get_filename_from_path, p_help
from hash_file import hash_file_from_absolute_path

def sys_print_hash():
    path = sys.argv[1]
    file_name = get_filename_from_path(path)
    try:
        blake_hash = hash_file_from_absolute_path(path)
    except:
        p_help()
        raise FileNotFoundError
    print(f"The hash of {file_name} is:\n{blake_hash.hexdigest()}")

