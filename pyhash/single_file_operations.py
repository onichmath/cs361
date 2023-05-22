import hash_file
from questions import question_single_file_path, question_confirm, single_file_prompt, question_single_directory, get_filename_from_path

def get_single_file_path_hash():
    while True:
        path = question_single_file_path() 
        try:
            blake_hash = hash_file.hash_file_from_absolute_path(path)
        except:
            print(FileNotFoundError("File not found"))
            if question_confirm("Try another path?"):
                continue
            else: 
                return None,None
        return path, blake_hash

def single_file_operations(path,hash):
    file_name = get_filename_from_path(path)
    while True:
        answer = single_file_prompt()
        if answer == "Print the hash to the terminal":
            print(f"The hash of {file_name} is:\n{hash.hexdigest()}")
            continue
        if answer == "Save the hash to a file":
            if question_confirm("Saving a hash will take up drive space. Continue?"):
                path = question_single_directory()
                hash_file.save_hash_to_absolute_path(hash,path + f"/{file_name}.blake2")
            continue
        if answer == "Return to start screen":
            return
