import questionary
from pprint import pprint
import hash_file
from re import split 



def main():
    while True:
        init_answer = start_screen()
        match init_answer:
            case "Help":
                p_help()
            case "Single File Operations":
                path,hash = get_single_file_path_hash()
                single_file_operations(path,hash)
            case "Exit":
                break
