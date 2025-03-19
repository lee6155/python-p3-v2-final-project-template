from models.__init__ import CONN, CURSOR

from models.user import User
from models.file import File

import fire

from helpers import (
    create_user,
    get_all_users,
    get_users_by_type,
    get_all_files,
    get_files_by_type,
    get_files_by_type_and_user,
    search_files_by_name_and_user,
    delete_selected_user,
    selected_user_create_file,
    selected_user_delete_file,
    selected_user_see_files,
    selected_user_search_files,
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
                print("2. See all users (additional functions available if selected)")
                print("3. See users by type")
                user_level_choice = input(">>> ")

                User.create_table()
                    
                if user_level_choice == "0":
                    secondary_menu = ""

                elif user_level_choice == "1":
                    create_user()

                elif user_level_choice == "2":
                    get_all_users()

                    level_three_menu = "3"
                    while level_three_menu == "3":
                        print("\033[4mPlease select an option\033[0m:")
                        print("0. Go back to previous menu")
                        print("1. Delete a user")
                        print("2. Create a file for a user")
                        print("3. Delete a file for a user")
                        print("4. See files by user")
                        print("5. For user, search files by file name")
                        level_three_choice = input(">>> ")

                        if level_three_choice  == "0":
                            level_three_menu = ""

                        if level_three_choice == "1":
                            delete_selected_user()

                        if level_three_choice == "2":
                            selected_user_create_file()
                            
                        if level_three_choice == "3":
                            selected_user_delete_file()

                        if level_three_choice == "4":
                            selected_user_see_files()

                        if level_three_choice == "5":
                            selected_user_search_files()
                        
                        else:              
                            print("Invalid choice")

                elif user_level_choice == "3":
                    get_users_by_type()
                        
                else:              
                    print("Invalid choice")
    
        elif main_choice == "2":
            secondary_menu = "file choices"
            while secondary_menu == "file choices":
                print("\033[4mFunctions for files\033[0m")
                print("\033[4mPlease select an option\033[0m:")
                print("0. Go back to previous menu")
                print("1. See all files")
                print("2. See files by type")
                print("3. See files by type and user")
                print("4. Search files by file name and user")
                file_level_choice = input(">>> ")

                File.create_table()
 
                if file_level_choice == "0":
                    secondary_menu = ""
                
                elif file_level_choice == "1":
                    get_all_files()
                
                elif file_level_choice == "2":
                    get_files_by_type()

                elif file_level_choice == "3":
                    get_files_by_type_and_user()
                
                elif file_level_choice == "4":
                    search_files_by_name_and_user()

                else:              
                    print("Invalid choice")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    fire.Fire(main)
