# lib/cli.py

from models.user import (
    User
)

from models.file import (
    File
    # create,
    # delete,
    # get_all,
    # find_by_id,
    # files_by_type,
    # files_by_user,
    # files_by_type_and_user,
    # number_files,
    # number_files_by_type,
    # number_files_by_user,
    # number_files_by_type_and_user,
    # search_file_name,
    # search_file_name_and_user,
    # count_searched_file_name,
    # count_searched_file_name_and_user
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
        main_choices = input(">>> ")

        if main_choices == "0":
            print("Goodbye!")
            exit()

        elif main_choices == "1":
            print("\033[4mFuntions for users\033[0m")
            print("\033[4mPlease select an option\033[0m:")
            print("0. Go back to previous menu")
            print("1. Create a user")
            print("2. Delete a user")
            print("3. See all users")
            print("***4. Find user by ID***")
            print("5. See users by type")
            print("6. Calculate total number of users")
            print("7. Calculate number of users by type")
            user_level_choices = input(">>> ")

            User.create_table()
                
            if user_level_choices == "1":
                print('\033[4mEnter username, then user type (without "")\033[0m:')
                username = input(">>> ")
                user_type = input(">>> ")
                User.create(username, user_type)
            elif user_level_choices == "2":
                print("\033[4mEnter user's ID\033[0m:")
                id = input(">>> ")
                User.delete(id)
            elif user_level_choices == "3":
                User.get_all()
            elif user_level_choices == "4":
                User.find_by_id()
            elif user_level_choices == "5":
                User.users_by_type()
            elif user_level_choices == "6":
                User.number_users()
            elif user_level_choices == "7":
                User.number_users_by_type
            else:              
                print("Invalid choice")    

        elif main_choices == "2":
            print("Functions for files")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    fire.Fire(main)
