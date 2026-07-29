import os

from constants import MASTER_PASSWORD_FILE

from auth import (
    create_master_password,
    check_master_password,
    change_master_password
)

from manager import (
    add_password,
    view_passwords,
    search_password,
    delete_password
)



def password_menu():

    while True:

        print("\n==============================")
        print("       PASSWORD MANAGER")
        print("==============================")

        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Change Master Password")
        print("6. Exit")



        choice = input("\nChoose an option: ")



        if choice == "1":

            add_password()



        elif choice == "2":

            view_passwords()



        elif choice == "3":

            search_password()



        elif choice == "4":

            delete_password()



        elif choice == "5":

            change_master_password()



        elif choice == "6":

            print("\nGoodbye!")

            break



        else:

            print("\nInvalid option!")





def main():

    print("==============================")
    print("       PASSWORD MANAGER")
    print("==============================")


    if not os.path.exists(MASTER_PASSWORD_FILE):

        created = create_master_password()


        if created:

            password_menu()



    else:


        logged_in = check_master_password()


        if logged_in:

            password_menu()





if __name__ == "__main__":

    main()