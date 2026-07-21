# ============================================
# encryption.py
# This file is responsible for encrypting
# and decrypting the passwords
# ============================================

import base64

from constants import SECRET_KEY


# ============================================
# password encryption
# ============================================

def encrypt(password):

    encrypted_characters = ""

    key_length = len(SECRET_KEY)

    key_position = 0

    for character in password:

        key_character = SECRET_KEY[key_position]

        encrypted_character = chr(ord(character) ^ ord(key_character))

        encrypted_characters = encrypted_characters + encrypted_character

        key_position = key_position + 1

        if key_position == key_length:

            key_position = 0


    encrypted_bytes = encrypted_characters.encode()

    base64_bytes = base64.b64encode(encrypted_bytes)

    encrypted_text = base64_bytes.decode()

    return encrypted_text


# ============================================
# password decryption
# ============================================

def decrypt(encrypted_password):

    base64_bytes = encrypted_password.encode()

    encrypted_bytes = base64.b64decode(base64_bytes)

    encrypted_text = encrypted_bytes.decode()

    decrypted_password = ""

    key_length = len(SECRET_KEY)

    key_position = 0


    for character in encrypted_text:

        key_character = SECRET_KEY[key_position]

        original_character = chr(ord(character) ^ ord(key_character))

        decrypted_password = decrypted_password + original_character

        key_position = key_position + 1

        if key_position == key_length:

            key_position = 0

    return decrypted_password