from json import loads, dump
from tkinter import Button, Entry

from May2023.GUI_Shop.buying_page import display_products
from May2023.GUI_Shop.canvas import root, frame
from May2023.GUI_Shop.helpers import clean_screen, get_password_hash


def render_entry():
    register_button = Button(
        root,
        text="Register",
        # bg="green", ## not working on MacOS
        # fg="white",
        width=20,
        borderwidth=0,
        height=3,
        command=register
    )
    login_button = Button(
        root,
        text="Login",
        # bg="blue",
        # fg="white",
        width=20,
        borderwidth=0,
        height=3,
        command=login,
    )
    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 320, window=login_button)


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username")
    frame.create_text(100, 100, text="Password")

    frame.create_window(250, 50, window=user_name_box)
    frame.create_window(250, 100, window=pass_box)

    login_button = Button(
        root,
        text="Login",
        command=logging
    )

    frame.create_window(250, 150, window=login_button)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(360, 200, text="Invalid username or password", fill="red")


def check_logging():
    info_data = get_users_data()

    user_username = user_name_box.get()
    user_password = get_password_hash(pass_box.get())

    for record in info_data:
        record_username = record["Username"]
        record_password = record["Password"]

        if user_username == record_username and user_password == record_password:
            return True

    return False


def get_users_data():
    info_data = []

    with open("db/users_info.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def register():
    clean_screen()

    frame.create_text(100, 50, text="First Name")
    frame.create_text(100, 100, text="Last Name")
    frame.create_text(100, 150, text="User Name")
    frame.create_text(100, 200, text="Password")

    frame.create_window(250, 50, window=first_name_box)
    frame.create_window(250, 100, window=last_name_box)
    frame.create_window(250, 150, window=user_name_box)
    frame.create_window(250, 200, window=pass_box)

    register_button = Button(
        root,
        text="Register",
        command=registration,
    )

    frame.create_window(300, 250, window=register_button)


def registration():
    info_dict = {
        "First Name": first_name_box.get(),
        "Last Name": last_name_box.get(),
        "Username": user_name_box.get(),
        "Password": pass_box.get(),
    }

    print(info_dict)

    if check_registration(info_dict):
        with open("db/users_info.txt", "a") as users_file:
            info_dict["Password"] = get_password_hash(info_dict["Password"])
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()


def check_registration(info):
    frame.delete('error')
    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",
            )

            return False

    info_data = get_users_data()
    for record in info_data:
        if record["Username"] == info["Username"]:
            frame.create_text(
                300,
                300,
                text="Username is taken",
                fill="red",
                tags="error",
            )
            return False

    return True


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
user_name_box = Entry(root, bd=0)
pass_box = Entry(root, bd=0, show="*")
