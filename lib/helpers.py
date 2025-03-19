from models.__init__ import CONN, CURSOR

from models.user import User
from models.file import File

def create_user():
    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    print('\033[4mEnter user type (without ""), then press enter\033[0m:')
    user_type = input(">>> ")

    User.create(username, user_type)
    print("User created!")

def get_all_users():
    users = User.get_all()

    if users != []:
        for i, user in enumerate(users):
            print(f"{i+1}. Username: {user.username}, User Type: {user.user_type}")
    else:
        print("No users found")

def get_users_by_type():
    print('\033[4mEnter user type (without ""), then press enter\033[0m:')
    user_type = input(">>> ")

    if user_type != "personal" and user_type != "business":
        raise ValueError("The user type must be either personal or business")
    
    users = User.users_by_type(user_type)

    if users != []:
        print("Users found!")
        for user in users:
            print(f"Username: {user.username}")
    else:
        print("No users found")
                
def get_all_files():
    files = File.get_all()

    if files != []:
        print("Files found!")

        for file in files:
            print(f'File Name: {file.file_name}, File Type: {file.file_type}, Description: {file.description}, Username: {file.username}')

    else:
        print("No files found")
                
def get_files_by_type():
    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type = input(">>> ")
    
    if file_type != ".doc" and file_type != ".xls" and file_type != ".ppt" and file_type != ".pdf":
        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")
    
    files = File.files_by_type(file_type)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'File Name: {file.file_name}, Description: {file.description}, Username: {file.username}')

    else:
        print("No files found")

def get_files_by_type_and_user():
    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type_selected = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    if file_type_selected != ".doc" and file_type_selected != ".xls" and file_type_selected != ".ppt" and file_type_selected != ".pdf":
        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")

    files = File.files_by_type_and_user(file_type_selected, username)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'File Name: {file.file_name}, Description: {file.description}')

    else:
        print("No files found")
                
def search_files_by_name_and_user():
    print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
    search_term = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")
    
    files = File.search_file_name_and_user(search_term, username)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'File Name: {file.file_name}, File Type: {file.file_type}, Description: {file.description}')

    else:
        print("No files found")

def get_username_from_selected_user():
    print("\033[4mPlease select the number of the user, then press enter\033[0m:")
    user_string = input(">>> ")
    user_number = int(user_string)

    all_users = User.get_all()
    selected_username = all_users[user_number-1].username
    return selected_username

def delete_selected_user():
    username = get_username_from_selected_user()

    instance = User.select_by_username(username)
    instance.delete()

    print("User deleted!")

def selected_user_create_file():
    username = get_username_from_selected_user()

    print('\033[4mEnter file name (without ""), then press enter\033[0m:')
    file_name = input(">>> ")

    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type = input(">>> ")

    print('\033[4mEnter description (without ""), then press enter\033[0m:')
    description = input(">>> ")
    
    File.create(file_name, file_type, description, username)

    print("File created!")

def selected_user_delete_file():
    username = get_username_from_selected_user()
    
    files = File.files_by_user(username)
    for file in files:
        print(f'File Name: {file.file_name}, File Type: {file.file_type}, Description: {file.description}')

    print('\033[4mEnter file name (without ""), then press enter\033[0m:')
    file_name = input(">>> ")

    instance = File.file_by_name_and_user(file_name, username)
        
    if instance != None:
        print("File deleted!")
        instance.delete()
    else:
        print("No file found")

def selected_user_see_files():
    username = get_username_from_selected_user()
    
    files = File.files_by_user(username)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'File Name: {file.file_name}, File Type: {file.file_type}, Description: {file.description}')

    else:
        print("No files found")

def selected_user_search_files():
    username = get_username_from_selected_user()

    print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
    search_term = input(">>> ")

    files = File.search_file_name_and_user(search_term, username)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'File Name: {file.file_name}, File Type: {file.file_type}, Description: {file.description}')

    else:
        print("No files found")
