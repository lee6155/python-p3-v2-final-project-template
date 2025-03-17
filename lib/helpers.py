from models.__init__ import CONN, CURSOR

from models.user import User
from models.file import File

def get_id_from_username(username):
    sql = """
        SELECT id
        FROM users
        WHERE username = ?
    """

    row = CURSOR.execute(sql, (username,)).fetchone()

    if row == None:
        return "0"
    else:
        return row[0]

def create_user():
    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    print('\033[4mEnter user type (without ""), then press enter\033[0m:')
    user_type = input(">>> ")

    User.create(username, user_type)
    print("User created!")

def delete_user():
    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    def select_by_username(username):
        sql = """
            SELECT *
            FROM users
            WHERE username = ?
        """

        row = CURSOR.execute(sql, (username,)).fetchone()
        instance = User.instance_from_db(row) if row else None

        if instance != None:
            print("User deleted!")
            instance.delete()
        else:
            print("No user found")

    select_by_username(username)

def get_all_users():
    users = User.get_all()

    if users != []:
        print("Users found!")
        for user in users:
            print(f"{user.username}, {user.user_type}")
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
            print(f"{user.username}")
    else:
        print("No users found")

def number_users():
    print(f'Total number of users: {User.number_users()}')

def number_users_by_type():
    print('\033[4mEnter user type (without ""), then press enter\033[0m:')
    user_type = input(">>> ")

    if user_type != "personal" and user_type != "business":
        raise ValueError("The user type must be either personal or business")
    
    print(f'Number of {user_type} users: {User.number_users_by_type(user_type)}')
                    
def create_file():
    print('\033[4mEnter file name (without ""), then press enter\033[0m:')
    file_name = input(">>> ")

    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type = input(">>> ")

    print('\033[4mEnter description (without ""), then press enter\033[0m:')
    description = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    id = get_id_from_username(username)

    File.create(file_name, file_type, description, id)

    print("File created!")
                
def delete_file():
    print('\033[4mEnter file name (without ""), then press enter\033[0m:')
    file_name = input(">>> ")

    def select_by_file_name(file_name):
        sql = """
            SELECT *
            FROM files
            WHERE file_name = ?
        """

        row = CURSOR.execute(sql, (file_name,)).fetchone()
        instance = File.instance_from_db(row) if row else None
        
        if instance != None:
            print("File deleted!")
            instance.delete()
        else:
            print("No file found")

    select_by_file_name(file_name)

    print("File deleted!")
                
def get_all_files():
    files = File.get_all()

    if files != []:
        print("Files found!")

        for file in files:
            print(f'{file.file_name}, {file.file_type}, {file.description}, {File.get_username_from_user_id(file.user_id)}')

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
            print(f'{file.file_name}, {file.description}, {File.get_username_from_user_id(file.user_id)}')

    else:
        print("No files found")

def get_files_by_user():
    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    id = get_id_from_username(username)
    files = File.files_by_user(id)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'{file.file_name}, {file.file_type}, {file.description}')

    else:
        print("No files found")

def get_files_by_type_and_user():
    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    if file_type != ".doc" and file_type != ".xls" and file_type != ".ppt" and file_type != ".pdf":
        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")

    id = get_id_from_username(username)
    files = File.files_by_type_and_user(file_type, id)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'{file.file_name}, {file.description}')

    else:
        print("No files found")
                
def number_files():
    print(f'Total number of files: {File.number_files()}')
                
def number_files_by_type():
    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type = input(">>> ")

    if file_type != ".doc" and file_type != ".xls" and file_type != ".ppt" and file_type != ".pdf":
        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")
    
    print(f'Number of {file_type} files: {File.number_files_by_type(file_type)}')
                
def number_files_by_user():
    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    id = get_id_from_username(username)

    print(f'Number of files for {username}: {File.number_files_by_user(id)}')
                
def number_files_by_type_and_user():
    print('\033[4mEnter file type (without ""), then press enter\033[0m:')
    file_type = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    id = get_id_from_username(username)

    print(f'Number of {file_type} files for {username}: {File.number_files_by_type_and_user(file_type, id)}')
                
def search_files_by_name():
    print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
    search_term = input(">>> ")

    files = File.search_file_name(search_term)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'{file.file_name}, {file.file_type}, {file.description}, {File.get_username_from_user_id(file.user_id)}')

    else:
        print("No files found")
                
def search_files_by_name_and_user():
    print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
    search_term = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")
    
    id = get_id_from_username(username)
    files = File.search_file_name_and_user(search_term, id)

    if files != []:
        print("Files found!")

        for file in files:
            print(f'{file.file_name}, {file.file_type}, {file.description}')

    else:
        print("No files found")
                
def number_files_by_searched_name():
    print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
    search_term = input(">>> ")

    print(f'Total number of files: {File.count_searched_file_name(search_term)}')
                
def number_files_by_searched_name_and_user():
    print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
    search_term = input(">>> ")

    print('\033[4mEnter username (without ""), then press enter\033[0m:')
    username = input(">>> ")

    id = get_id_from_username(username)

    print(f'Total number of files: {File.count_searched_file_name_and_user(search_term, id)}')