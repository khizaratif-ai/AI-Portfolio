import os

# Main project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data folder
DATA_FOLDER = os.path.join(BASE_DIR, "data")

# Files
MASTER_PASSWORD_FILE = os.path.join(DATA_FOLDER, "master.hash")
PASSWORD_FILE = os.path.join(DATA_FOLDER, "passwords.json")


# Create data folder if it does not exist
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)