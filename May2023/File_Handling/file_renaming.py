import os
import re

directory = input("Enter a directory: ")
to_replace = input("Enter symbol to be replaced: ")
replace_with = input("Enter symbol to replace with: ")

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    print(file)
    if os.path.isfile(file):
        new_name = filename.replace(to_replace, replace_with)
        print(new_name)
        new_file = '/'.join(re.split(r'[\\/]', file)[:-1]) + "/" + new_name
        print(new_file)
        os.rename(file, new_file)
