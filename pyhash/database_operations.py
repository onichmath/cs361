import hash_file 
from questions import question_single_file_path, get_filename_from_path, question_confirm
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
