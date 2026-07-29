import hashlib
import os

from constants import MASTER_PASSWORD_FILE


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()



def create_master_password():

    print("\nCreate your master password")

    password = input("Enter master password: ")

    confirm_password = input("Confirm master password: ")


    if password != confirm_password:

        print("Passwords do not match!")

        return False


    hashed_password = hash_password(password)


    with open(MASTER_PASSWORD_FILE, "w") as file:

        file.write(hashed_password)


    print("\nMaster password created successfully!")

    return True





def check_master_password():

    if not os.path.exists(MASTER_PASSWORD_FILE):

        return False


    password = input("\nEnter master password: ")


    with open(MASTER_PASSWORD_FILE, "r") as file:

        saved_password = file.read()



    if hash_password(password) == saved_password:

        print("Login successful!")

        return True


    else:

        print("Wrong password!")

        return False





def change_master_password():

    print("\n===== Change Master Password =====")


    current_password = input("Enter current master password: ")



    with open(MASTER_PASSWORD_FILE, "r") as file:

        saved_password = file.read()



    if hash_password(current_password) != saved_password:

        print("Wrong current password!")

        return False




    new_password = input("Enter new master password: ")

    confirm_password = input("Confirm new master password: ")



    if new_password != confirm_password:

        print("Passwords do not match!")

        return False




    new_hash = hash_password(new_password)



    with open(MASTER_PASSWORD_FILE, "w") as file:

        file.write(new_hash)



    print("\nMaster password changed successfully!")

    return True