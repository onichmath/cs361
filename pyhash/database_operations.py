"""
Author: Matthew O'Malley-Nichols
Description: Database operations for use with cli
"""
import hash_file 
from questions import question_single_file_path, get_filename_from_path, question_confirm, query_database_type_prompt, database_operations_prompt
from database import client
from datetime import datetime

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
            query = f"INSERT INTO hashes (hash,file_name, timestamp) VALUES ('{blake_hash.hexdigest()}', '{file_name}', '{datetime.now()}')"
            print(query)
            client.client(query)
        except:
            print("server error")
        return

def database_select_single_file():
    while True:
        file_name = input("Filename to get:")
        query = f"SELECT file_name, timestamp, hash FROM hashes WHERE file_name = '{file_name}'"
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
        if answer == "Get a single file hash":
            database_select_single_file()
            continue
        if answer == "Get all file hashes":
            hash_query_results = client.client("SELECT file_name, timestamp, hash FROM hashes")
            if hash_query_results:
                for row in hash_query_results:
                    print(row)
            continue
        if answer == "Return to previous screen":
            return

def database_operations():
    while True:
        answer = database_operations_prompt()
        if answer == "Add a file hash to database":
            add_file_hash_to_database()
            continue
        if answer == "Query the database for file hash":
            query_database()
            continue
        if answer == "Return to start screen":
            return
