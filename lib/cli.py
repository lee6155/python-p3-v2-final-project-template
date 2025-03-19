from models.__init__ import CONN, CURSOR

from models.user import User
from models.file import File

import fire

from helpers import (
    create_user,
    delete_user,
    get_all_users,
    get_users_by_type,
    number_users,
    number_users_by_type,
    create_file,
    delete_file,
    get_all_files,
    get_files_by_type,
    get_files_by_user,
    get_files_by_type_and_user,
    number_files,
    number_files_by_type,
    number_files_by_user,
    number_files_by_type_and_user,
    search_files_by_name,
    search_files_by_name_and_user,
    number_files_by_searched_name,
    number_files_by_searched_name_and_user,
    get_id_from_username
)

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
                print("\033[4mFunctions for users\033[0m")
                print("\033[4mPlease select an option\033[0m:")
                print("0. Go back to previous menu")
                print("1. Create a user")
                print("2. Delete a user")
                print("3. See all users (additional functions available if selected)")
                print("4. See users by type")
                print("5. Calculate total number of users")
                print("6. Calculate number of users by type")
                user_level_choice = input(">>> ")

                User.create_table()
                    
                if user_level_choice == "0":
                    secondary_menu = ""

                elif user_level_choice == "1":
                    create_user()

                elif user_level_choice == "2":
                    delete_user()

                elif user_level_choice == "3":
                    get_all_users()

                    level_three_menu = "3"
                    while level_three_menu == "3":
                        print("\033[4mPlease select an option\033[0m:")
                        print("0. Go back to previous menu")
                        print("1. Delete a user")
                        print("2. Create a file for a user")
                        print("3. Delete a file for a user")
                        print("4. See files by user")
                        print("5. Calculate number of files by user")
                        print("6. For user, search files by file name")
                        print("7. For user, calculate number of matches when searching by file name")
                        level_three_choice = input(">>> ")

                        if level_three_choice  == "0":
                            level_three_menu = ""

                        def get_id_from_selected_user():
                            print("\033[4mPlease select the number of the user, then press enter\033[0m:")
                            user_string = input(">>> ")
                            user_number = int(user_string)

                            all_users = User.get_all()
                            selected_username = all_users[user_number-1].username
                            id = get_id_from_username(selected_username)
                            return id

                        if level_three_choice == "1":
                            def delete_selected_user():
                                print("\033[4mPlease select the number of the user, then press enter\033[0m:")
                                user_string = input(">>> ")
                                user_number = int(user_string)

                                all_users = User.get_all()
                                selected_username = all_users[user_number-1].username

                                def select_by_username(selected_username):
                                    sql = """
                                        SELECT *
                                        FROM users
                                        WHERE username = ?
                                    """

                                    row = CURSOR.execute(sql, (selected_username,)).fetchone()
                                    instance = User.instance_from_db(row) if row else None
                                    instance.delete()

                                    print("User deleted!")

                                select_by_username(selected_username)
                                
                            delete_selected_user()

                        if level_three_choice == "2":
                            def selected_user_create_file():
                                id = get_id_from_selected_user()

                                print('\033[4mEnter file name (without ""), then press enter\033[0m:')
                                file_name = input(">>> ")

                                print('\033[4mEnter file type (without ""), then press enter\033[0m:')
                                file_type = input(">>> ")

                                print('\033[4mEnter description (without ""), then press enter\033[0m:')
                                description = input(">>> ")
                                
                                File.create(file_name, file_type, description, id)

                                print("File created!")

                            selected_user_create_file()
                            
                        if level_three_choice == "3":
                            def selected_user_delete_file():
                                id = get_id_from_selected_user()
                                
                                print('\033[4mEnter file name (without ""), then press enter\033[0m:')
                                file_name = input(">>> ")

                                def select_by_file_name_and_username(file_name, id):
                                    sql = """
                                        SELECT *
                                        FROM files
                                        WHERE file_name = ? AND user_id = ?
                                    """

                                    row = CURSOR.execute(sql, (file_name, id)).fetchone()
                                    instance = File.instance_from_db(row) if row else None
                                    
                                    if instance != None:
                                        print("File deleted!")
                                        instance.delete()
                                    else:
                                        print("No file found")

                                select_by_file_name_and_username(file_name, id)

                            selected_user_delete_file()

                        if level_three_choice == "4":
                            def selected_user_see_files():
                                id = get_id_from_selected_user()
                                
                                files = File.files_by_user(id)

                                if files != []:
                                    print("Files found!")

                                    for file in files:
                                        print(f'{file.file_name}, {file.file_type}, {file.description}')

                                else:
                                    print("No files found")
                            
                            selected_user_see_files()

                        if level_three_choice == "5":
                            def selected_user_count_files():
                                id = get_id_from_selected_user()

                                print(f'Number of files for {File.get_username_from_user_id(id)}: {File.number_files_by_user(id)}')
                            
                            selected_user_count_files()
                        
                        if level_three_choice == "6":
                            def selected_user_search_files():
                                id = get_id_from_selected_user()

                                print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
                                search_term = input(">>> ")

                                files = File.search_file_name_and_user(search_term, id)

                                if files != []:
                                    print("Files found!")

                                    for file in files:
                                        print(f'{file.file_name}, {file.file_type}, {file.description}')

                                else:
                                    print("No files found")

                            selected_user_search_files()
                        
                        if level_three_choice == "7":
                            def selected_user_count_searched_files():
                                id = get_id_from_selected_user()
                                
                                print('\033[4mEnter search term for file name (without ""), then press enter\033[0m:')
                                search_term = input(">>> ")

                                print(f'Total number of files: {File.count_searched_file_name_and_user(search_term, id)}')

                            selected_user_count_searched_files()

                elif user_level_choice == "4":
                    get_users_by_type()

                elif user_level_choice == "5":
                    number_users()

                elif user_level_choice == "6":
                    number_users_by_type()
                        
                else:              
                    print("Invalid choice")
    
        elif main_choice == "2":
            secondary_menu = "file choices"
            while secondary_menu == "file choices":
                print("\033[4mFunctions for files\033[0m")
                print("\033[4mPlease select an option\033[0m:")
                print("0. Go back to previous menu")
                print("1. Create a file")
                print("2. Delete a file")
                print("---------------------------------------------------------------------")
                print("3. See all files")
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
 
                if file_level_choice == "0":
                    secondary_menu = ""

                elif file_level_choice == "1":
                    create_file()

                elif file_level_choice == "2":
                    delete_file()
                
                elif file_level_choice == "3":
                    get_all_files()
                
                elif file_level_choice == "4":
                    get_files_by_type()
                
                elif file_level_choice == "5":
                    get_files_by_user()

                elif file_level_choice == "6":
                    get_files_by_type_and_user()
                
                elif file_level_choice == "7":
                    number_files()
                
                elif file_level_choice == "8":
                    number_files_by_type()
                
                elif file_level_choice == "9":
                    number_files_by_user()
                
                elif file_level_choice == "10":
                    number_files_by_type_and_user()
                
                elif file_level_choice == "11":
                    search_files_by_name()
                
                elif file_level_choice == "12":
                    search_files_by_name_and_user()         
                
                elif file_level_choice == "13":
                    number_files_by_searched_name()
                
                elif file_level_choice == "14":
                    number_files_by_searched_name_and_user()
                else:              
                    print("Invalid choice")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    fire.Fire(main)
