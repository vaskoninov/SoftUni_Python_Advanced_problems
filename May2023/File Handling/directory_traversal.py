import os


def save_extensions(dir_name):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file_name)

        elif os.path.isdir(file):
            save_extensions(file)


directory = input()

extensions = {}
try:
    save_extensions(directory)
except FileNotFoundError:
    print("No such file or directory")

extensions = {k: sorted(v) for k, v in sorted(extensions.items(), key=lambda x: x[0])}

for key, values in extensions.items():
    print(f".{key}")
    for value in values:
        print(f"- - - {value}")
