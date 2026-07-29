# ==========================
# database.py
# This file loads and saves
# passwords from the JSON file.
# ==========================

import json
import os

from constants import PASSWORD_FILE


# Create the password file if it does not exist
def create_password_file():

    folder = os.path.dirname(PASSWORD_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(PASSWORD_FILE):

        with open(PASSWORD_FILE, "w") as file:
            json.dump([], file, indent=4)


# Load all passwords
def load_passwords():

    create_password_file()

    try:

        with open(PASSWORD_FILE, "r") as file:
            passwords = json.load(file)

    except json.JSONDecodeError:

        passwords = []

    return passwords


# Save passwords
def save_passwords(password_list):

    with open(PASSWORD_FILE, "w") as file:
        json.dump(password_list, file, indent=4)