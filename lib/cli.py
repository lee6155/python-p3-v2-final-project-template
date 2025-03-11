# lib/cli.py

from models.__init__ import CONN, CURSOR

from models.user import (
    User
)

from models.file import (
    File
)

import fire


def main():
    menu = "main"
    while menu == "main":
        print("\033[4mMain menu\033[0m")
        print("\033[4mPlease select an option\033[0m:")
        print("0. Exit the program")
        print("1. Functions for users")
        print("2. Functions for files")
        main_choice = input(">>> ")

        if main_choice == "0":
            print("Goodbye!")
            exit()

        elif main_choice == "1":
            secondary_menu = "user choices"
            while secondary_menu == "user choices":
                print("\033[4mFuntions for users\033[0m")
                print("\033[4mPlease select an option\033[0m:")
                print("0. Go back to previous menu")
                print("1. Create a user")
                print("2. Delete a user")
                print("3. See all users")
                # print("4. Find user by ID")
                print("4. See users by type")
                print("5. Calculate total number of users")
                print("6. Calculate number of users by type")
                user_level_choice = input(">>> ")

                User.create_table()
                    
                if user_level_choice == "0":
                    secondary_menu = ""

                elif user_level_choice == "1":
                    print('\033[4mEnter username, then user type (without "")\033[0m:')
                    username = input(">>> ")
                    user_type = input(">>> ")
                    User.create(username, user_type)
                    print("User created!")

                elif user_level_choice == "2":
                    print('\033[4mEnter username (without "")\033[0m:')
                    username = input(">>> ")

                    def cli_delete(username):
                        sql = """
                            SELECT *
                            FROM users
                            WHERE username = ?
                        """

                        row = CURSOR.execute(sql, (username,)).fetchone()
                        instance = User.instance_from_db(row) if row else None
                        instance.delete()

                    cli_delete(username)
                    print("User deleted!")

                elif user_level_choice == "3":
                    if User.get_all() != []:
                        print(User.get_all())
                        print("Users found!")
                    else:
                        print("No users found")

                # elif user_level_choice == "4":
                #     User.find_by_id()

                elif user_level_choice == "4":
                    print('\033[4mEnter user type (without "")\033[0m:')
                    user_type = input(">>> ")
                    if user_type != "personal" and user_type != "business":
                        raise ValueError("The user type must be either personal or business")
                    
                    if User.users_by_type(user_type) != []:
                        print(User.users_by_type(user_type))
                        print("Users found!")
                    else:
                        print("No users found")

                elif user_level_choice == "5":
                    print(f'Total number of users: {User.number_users()}')

                elif user_level_choice == "6":
                    print('\033[4mEnter user type (without "")\033[0m:')
                    user_type = input(">>> ")
                    if user_type != "personal" and user_type != "business":
                        raise ValueError("The user type must be either personal or business")
                    
                    print(f'Number of {user_type} users: {User.number_users_by_type(user_type)}')
                        
                else:              
                    print("Invalid choice")    

        elif main_choice == "2":
            secondary_menu = "file choices"
            while secondary_menu == "file choices":
                print("\033[4mFuntions for files\033[0m")
                print("\033[4mPlease select an option\033[0m:")
                print("0. Go back to previous menu")
                print("1. Create a file")
                print("2. Delete a file")
                print("---------------------------------------------------------------------")
                print("3. See all files")
                # print("4. Find file by ID")
                print("4. See files by type")
                print("5. See files by user")
                print("6. See files by type and user")
                print("7. Calculate total number of files")
                print("8. Calculate number of files by type")
                print("9. Calculate number of files by user")
                print("10. Calculate number of files by type and user")
                print("---------------------------------------------------------------------")
                print("11. Search files by file name")
                print("12. Search files by file name and user")
                print("13. Calculate number of matches when searching by file name")
                print("14. Calculate number of matches when searching by file name and user")
                file_level_choice = input(">>> ")

                File.create_table()

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
                    
                if file_level_choice == "0":
                    secondary_menu = ""

                elif file_level_choice == "1":
                    print('\033[4mEnter file name, then the file type, description and user name (without "")\033[0m:')
                    file_name = input(">>> ")
                    file_type = input(">>> ")
                    description = input(">>> ")
                    username = input(">>> ")

                    id = get_id_from_username(username)

                    File.create(file_name, file_type, description, id)

                    print("File created!")
                
                elif file_level_choice == "2":
                    print('\033[4mEnter file name (without "")\033[0m:')
                    file_name = input(">>> ")

                    def cli_delete(file_name):
                        sql = """
                            SELECT *
                            FROM files
                            WHERE file_name = ?
                        """

                        row = CURSOR.execute(sql, (file_name,)).fetchone()
                        instance = File.instance_from_db(row) if row else None
                        instance.delete()

                    cli_delete(file_name)
                    print("File deleted!")
                
                elif file_level_choice == "3":
                    if File.get_all() != []:
                        print(File.get_all())
                        print("Files found!")
                    else:
                        print("No files found")
                
                elif file_level_choice == "4":
                    print('\033[4mEnter file type (without "")\033[0m:')
                    file_type = input(">>> ")
                    
                    if file_type != ".doc" and file_type != ".xls" and file_type != ".ppt" and file_type != ".pdf":
                        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")
                    
                    if File.files_by_type(file_type) != []:
                        print(File.files_by_type(file_type))
                        print("Files found!")
                    else:
                        print("No files found")

                elif file_level_choice == "5":
                    print('\033[4mEnter username (without "")\033[0m:')
                    username = input(">>> ")

                    id = get_id_from_username(username)
                    
                    if File.files_by_user(id) != []:
                        print(File.files_by_user(id))
                        print("Files found!")
                    else:
                        print("No files found")
                
                elif file_level_choice == "6":
                    print('\033[4mEnter file type, then username (without "")\033[0m:')
                    file_type = input(">>> ")
                    username = input(">>> ")

                    if file_type != ".doc" and file_type != ".xls" and file_type != ".ppt" and file_type != ".pdf":
                        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")

                    id = get_id_from_username(username)
                    
                    if File.files_by_type_and_user(file_type, id) != []:
                        print(File.files_by_type_and_user(file_type, id))
                        print("Files found!")
                    else:
                        print("No files found")
                
                elif file_level_choice == "7":
                    print(f'Total number of files: {File.number_files()}')
                
                elif file_level_choice == "8":
                    print('\033[4mEnter file type (without "")\033[0m:')
                    file_type = input(">>> ")

                    if file_type != ".doc" and file_type != ".xls" and file_type != ".ppt" and file_type != ".pdf":
                        raise ValueError("The file type must be either .doc, .xls, .ppt or .pdf")
                    
                    print(f'Number of {file_type} files: {File.number_files_by_type(file_type)}')
                
                elif file_level_choice == "9":
                    print('\033[4mEnter username (without "")\033[0m:')
                    username = input(">>> ")

                    id = get_id_from_username(username)

                    print(f'Number of files for {username}: {File.number_files_by_user(id)}')              
                
                elif file_level_choice == "10":
                    print('\033[4mEnter file type, then user (without "")\033[0m:')
                    file_type = input(">>> ")
                    username = input(">>> ")

                    id = get_id_from_username(username)

                    print(f'Number of {file_type} files for {username}: {File.number_files_by_type_and_user(file_type, id)}')
                
                elif file_level_choice == "11":
                    print('\033[4mEnter search term (without "")\033[0m:')
                    search_term = input(">>> ")

                    if File.search_file_name(search_term) != []:
                        print(File.search_file_name(search_term))
                    else:
                        print("No files found")
                
                elif file_level_choice == "12":
                    print('\033[4mEnter search term for file name, then username (without "")\033[0m:')
                    
                    search_term = input(">>> ")
                    username = input(">>> ")
                    
                    id = get_id_from_username(username)

                    if File.search_file_name_and_user(search_term, id) != []:
                        print(File.search_file_name_and_user(search_term, id))
                    else:
                        print("No files found")              
                
                elif file_level_choice == "13":
                    print('\033[4mEnter search term (without "")\033[0m:')
                    search_term = input(">>> ")

                    print(f'Total number of files: {File.count_searched_file_name(search_term)}')
                
                elif file_level_choice == "14":
                    print('\033[4mEnter search term for file name, then username (without "")\033[0m:')

                    search_term = input(">>> ")
                    username = input(">>> ")

                    id = get_id_from_username(username)

                    print(f'Total number of files: {File.count_searched_file_name_and_user(search_term, id)}')

                else:              
                    print("Invalid choice")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    fire.Fire(main)
