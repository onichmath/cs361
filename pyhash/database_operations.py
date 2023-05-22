import hash_file 
from questions import question_single_file_path, get_filename_from_path, question_confirm, query_database_type_prompt
from database import client

def add_file_hash_to_database():
    while True:
        path = question_single_file_path()
        try:
            blake_hash = hash_file.hash_file_from_absolute_path(path)
            file_name = get_filename_from_path(path)
        except:
            print(FileNotFoundError("File not found"))
            if question_confirm("Try another path?"):
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
            if question_confirm("Try another file name?"):
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
