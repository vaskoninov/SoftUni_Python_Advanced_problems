import os

directory = input("Enter a directory: ")
to_replace = input("Enter symbol to be replaced: ")
replace_with = input("Enter symbol to replace with: ")

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    print(file)
