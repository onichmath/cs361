import questionary

def question_single_path():
    return questionary.path("Path including the file (/path/to/file.ext):").ask()

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
