import os

## Finds the path to a file
abs_path = os.path.dirname(os.path.abspath(__file__))
print(abs_path)
while True:
    instructions = input()

    ## Breaks the cycle
    if instructions == "End":
        break

    ## Provides commands and data
    command, file, *commands = instructions.split("-")
    file_path = os.path.join(abs_path, file)

    if command == "Create":
        with open(file_path, "w"):
            pass

    if command == "Add":
        content = commands
        with open(file_path, "a") as f:
            f.write(f"{content[0]}\n")

    if command == "Replace":
        old_string, new_string = commands
        try:
            with open(file_path, "r+") as f:
                text = f.read()
                text = text.replace(old_string, new_string)

                f.seek(0)
                f.write(text)

        except FileNotFoundError:
            print("An error occurred")

    if command == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")
