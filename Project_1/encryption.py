from cryptography.fernet import Fernet
import os

from constants import DATA_FOLDER


KEY_FILE = os.path.join(DATA_FOLDER, "data/secret.key")

def generate_key():

    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)



def load_key():

    with open(KEY_FILE, "rb") as file:
        return file.read()



def encrypt_data(data):

    generate_key()

    key = load_key()

    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(data.encode())

    return encrypted_data.decode()



def decrypt_data(data):

    generate_key()

    key = load_key()

    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(data.encode())

    return decrypted_data.decode()