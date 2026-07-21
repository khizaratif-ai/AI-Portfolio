# ============================================
# This file is responsible for:
# 1) Creating the master password
# 2) Hashing the password
# 3) Verifying the password
# ============================================

import hashlib
import os
import getpass

from constants import MASTER_PASSWORD_FILE

# ================================================
# the function below converts a password into hash
# ================================================

def hash_password(password):
    password_bytes = password.encode()
    hashed_password = hashlib.sha256(password_bytes)
    fina_hash = hashed_password.hexdigest()
    return fina_hash

# ===========================================================================
# this function create the master password only if it does not already exist.
# ===========================================================================

def create_master_password():
    if os.path.exists(MASTER_PASSWORD_FILE):
        return

    print("======================================")
    print("FIRST TIME SETUP")
    print("======================================")
    print()
    while True:
        master_password = getpass.getpass("Create Master Password: ")

        confirm_password = getpass.getpass("Confirm Password: ")

        print()

        if master_password != confirm_password:

            print("Passwords do not match.")
            print("Please try again.")
            print()

        elif master_password == "":

            print("Password cannot be empty.")
            print()

        else:

            hashed_password = hash_password(master_password)

            file = open(MASTER_PASSWORD_FILE, "w")

            file.write(hashed_password)

            file.close()

            print("Master Password Created Successfully.")
            print()

            break
# ===============================================
# the function below verifies the master password
# ===============================================

def verify_master_password():

    print("======================================")
    print("LOGIN")
    print("======================================")
    print()

    file = open(MASTER_PASSWORD_FILE, "r")

    saved_hash = file.read()

    file.close()

    attempts = 3

    while attempts > 0:

        entered_password = getpass.getpass("Enter Master Password: ")

        entered_hash = hash_password(entered_password)

        if entered_hash == saved_hash:

            print()
            print("Login Successful.")
            return True

        else:

            attempts = attempts - 1

            print()
            print("Incorrect Password.")

            if attempts > 0:

                print("Attempts Remaining:", attempts)
                print()

    print()
    print("Too many failed attempts.")

    return False
