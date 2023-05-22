import hash_file
from database import client
import sys
from questions import question_single_path

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

