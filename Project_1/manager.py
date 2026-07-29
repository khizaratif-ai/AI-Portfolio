import json
import os

from constants import PASSWORD_FILE
from encryption import encrypt_data, decrypt_data



def load_passwords():

    if not os.path.exists(PASSWORD_FILE):

        return []


    with open(PASSWORD_FILE, "r") as file:

        return json.load(file)





def save_passwords(passwords):

    with open(PASSWORD_FILE, "w") as file:

        json.dump(passwords, file, indent=4)





def add_password():

    print("\nAdd New Password")

    website = input("Website name: ")

    username = input("Username/Email: ")

    password = input("Password: ")


    encrypted_password = encrypt_data(password)


    passwords = load_passwords()


    new_password = {

        "website": website,

        "username": username,

        "password": encrypted_password

    }


    passwords.append(new_password)


    save_passwords(passwords)


    print("\nPassword saved successfully!")





def view_passwords():

    passwords = load_passwords()


    if len(passwords) == 0:

        print("\nNo passwords saved.")

        return



    print("\nSaved Passwords")

    print("--------------------")


    for index, item in enumerate(passwords, start=1):

        print("\nID:", index)

        print("Website:", item["website"])

        print("Username:", item["username"])

        print("Password:", decrypt_data(item["password"]))





def search_password():

    search = input("\nEnter website name: ").lower()


    passwords = load_passwords()


    found = False


    for item in passwords:


        if item["website"].lower() == search:


            print("\nPassword Found")

            print("----------------")

            print("Website:", item["website"])

            print("Username:", item["username"])

            print("Password:", decrypt_data(item["password"]))


            found = True



    if not found:

        print("\nNo password found.")





def delete_password():

    passwords = load_passwords()


    if len(passwords) == 0:

        print("\nNo passwords available.")

        return



    view_passwords()


    try:

        number = int(input("\nEnter password ID to delete: "))


        passwords.pop(number - 1)


        save_passwords(passwords)


        print("\nPassword deleted successfully!")



    except:

        print("\nInvalid ID.")