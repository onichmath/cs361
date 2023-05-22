import questionary
import hash_file
from re import split 
import sys
from database import client
"""
Refactoring ideas:
    put each "line" of questions and functions into their own file
    try to improve composition by changing around file
    get rid of repeated code
    comment each function
"""

def start_screen() -> str:
    question = questionary.select(
            "Welcome to Hashy. Pick an option to continue:",
            choices=[
                "Single File Operations",
                "Database Operations",
                "Help",
                "Exit",
            ])
    return question.ask()

def single_file_prompt() -> str:
    question = questionary.select(
            "What would you like to do with the file's Blake2b hash?",
            choices = [
                "Print the hash to the terminal",
                "Save the hash to a file",
                "Return to start screen",
            ])
    return question.ask()

def database_operations_prompt() -> str:
    question = questionary.select(
            "What database operation would you like to make?",
            choices = [
                "Add a file hash to database",
                "Query the database for file hash",
                "Return to start screen",
                ])
    return question.ask()

def query_database_type_prompt() -> str:
    question = questionary.select(
            "What type of query would you like to make?",
            choices = [
                "Get a single file hash",
                "Get all file hashes",
                "Return to previous screen",
                ])
    return question.ask()

def p_help() -> None:
    print(f"\nWelcome to Hashy, a Command Line hashing tool. Hashy uses the Blake2 hashing algorithm to find the hashes of files. \
          \n\t1. Why? \
          \n\t\tTracking the hashes of files allows us to tell whether or not they have been tampered with. \
          \n\t2. How? \
          \n\t\tSimply follow the \"Single File Operations\" option and input a absolute path to a program \
          \n\t\tAbsolute paths: An absolute path form \"/path/to/file.ext\", where .ext is the file extension \
          \n\t3. Navigation \
          \n\t\tEither use arrow keys or j and k to move up and down. Use enter to select an option. \
          \n\t4. Alternate print format:\
          \n\t\tpython main.py \"/path/to/file.ext\" \
          \n\tTo continue, simply choose an option.\n")


def get_single_file_hash(path):
    return hash_file.hash_file_from_absolute_path(path)

def question_single_path():
    return questionary.path("Path including the file (/path/to/file.ext):").ask()

def get_filename_from_path(path):
    return split(r'^(.+)\/([^\/]+)$',path)[-2]

def get_single_file_path_hash():
    while True:
        path = question_single_path() 
        try:
            blake_hash = get_single_file_hash(path)
        except:
            print(FileNotFoundError("File not found"))
            if questionary.confirm("Try another path?").ask():
                continue
            else: 
                return None,None
        return path, blake_hash

def single_file_operations(path,hash):
    file_name = get_filename_from_path(path)
    while True:
        answer = single_file_prompt()
        match answer:
            case "Print the hash to the terminal":
                print(f"The hash of {file_name} is:\n{hash.hexdigest()}")
            case "Save the hash to a file":
                if questionary.confirm("Saving a hash will take up drive space. Continue?").ask():
                    path = questionary.path("Directory to save the hash:").ask()
                    hash_file.save_hash_to_absolute_path(hash,path + f"/{file_name}.blake2")
            case "Return to start screen":
                return

def sys_print_hash():
    path = sys.argv[1]
    file_name = get_filename_from_path(path)
    try:
        blake_hash = get_single_file_hash(path)
    except:
        p_help()
        raise FileNotFoundError
    print(f"The hash of {file_name} is:\n{blake_hash.hexdigest()}")

def add_file_hash_to_database():
    while True:
        path = question_single_path()
        try:
            blake_hash = get_single_file_hash(path)
            file_name = get_filename_from_path(path)
        except:
            print(FileNotFoundError("File not found"))
            if questionary.confirm("Try another path?").ask():
               continue 
            return
        try:
            #query = f"INSERT INTO hashes (hash,file_name) VALUES ('{blake_hash.hexdigest()}','{file_name}') WHERE NOT EXISTS (SELECT * FROM hashes WHERE file_name = '{file_name}' AND hash = '{blake_hash.hexdigest()}')"
            query = f"INSERT INTO hashes (hash,file_name) VALUES ('{blake_hash.hexdigest()}', '{file_name}')"
            print(query)
            client.client(query)
        except:
            print("server error")
        return


def database_select_single_file():
    while True:
        file_name = input("Filename to get:")
        query = f"SELECT hash, file_name FROM hashes WHERE file_name = '{file_name}'"
        try:
            client.client(query)
        except:
            print("Filename not found")
            if questionary.confirm("Try another file name?").ask():
                continue
        return

def query_database():
    while True:
        answer = query_database_type_prompt()
        match answer:
            case "Get a single file hash":
                database_select_single_file()
            case "Get all file hashes":
                hash_query_results = client.client("SELECT * FROM hashes")
                if hash_query_results:
                    for row in hash_query_results:
                        print(row)
            case "Return to previous screen":
                return

def database_operations():
    while True:
        answer = database_operations_prompt()
        match answer:
            case "Add a file hash to database":
                add_file_hash_to_database()
            case "Query the database for file hash":
                query_database()
            case "Return to start screen":
                return

def main():
    if len(sys.argv) == 1:
        while True:
            init_answer = start_screen()
            match init_answer:
                case "Help":
                    p_help()
                case "Single File Operations":
                    path,hash = get_single_file_path_hash()
                    if path:
                        single_file_operations(path,hash)
                case "Database Operations":
                    database_operations()
                case "Exit":
                    break
    else:
        sys_print_hash()
