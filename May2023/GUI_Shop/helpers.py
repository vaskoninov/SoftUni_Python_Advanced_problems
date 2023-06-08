from hashlib import sha256

from May2023.GUI_Shop.canvas import frame


def clean_screen():
    frame.delete("all")


def get_password_hash(password):
    hash_obj = sha256(password.encode())

    return str(hash_obj.hexdigest())
