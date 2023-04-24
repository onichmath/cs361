import questionary
from pprint import pprint
import hash_file
from re import split 
def start_screen():
    question = questionary.select(
            "Welcome to Hashy. Pick an option to continue:",
            choices=[
                "Single File Operations",
                "Help",
                "Exit",
            ])
    return question.ask()

def single_file_prompt():
    question = questionary.select(
            "What would you like to do with the file's Blake2b hash?",
            choices = [
                "Print the hash to the terminal",
                "Save the hash to a file",
                "Return to start screen",
            ])
    return question.ask()

def p_help():
    print("HELP OPTIONS HERE")


def get_single_file_hash(path):
    return hash_file.hash_file_from_absolute_path(path)

def question_single_path():
    return questionary.path("Path including the file:").ask()

def get_filename_from_path(path):
    return split(r'^(.+)\/([^\/]+)$',path)

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
                print(f"\nThe hash of {file_name[2]} is:\n{hash.hexdigest()}")
            case "Save the hash to a file":
                path = questionary.path("Path to save the hash:").ask()
                hash_file.save_hash_to_absolute_path(hash,path)
            case "Return to start screen":
                return

def main():
    while True:
        init_answer = start_screen()
        match init_answer:
            case "Help":
                p_help()
            case "Single File Operations":
                path,hash = get_single_file_path_hash()
                if path:
                    single_file_operations(path,hash)
            case "Exit":
                break
