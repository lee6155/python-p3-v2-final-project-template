from models.__init__ import CONN, CURSOR

from models.user import User
from models.file import File

import fire

# take a look at video of owners and dogs
# keep having to go back for long names, keep having to type

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
    number_files_by_searched_name_and_user
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
                print("3. See all users")
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
