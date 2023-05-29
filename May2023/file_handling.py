## Python File Object

# <class '_io.TextIOWrapper'>

### Reads a File
#
# try:
#     with open("text_file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found in the current directory.")


### Sums Numbers in a File
# with open('numbers.txt', "r") as file:
#     # result = 0
#     # for line in file:
#     #     result += int(line)
#     result = sum([int(line) for line in file])
#     print(result)


### Absolute Paths
#
# import os
#
# absolute_path = os.path.abspath(".")
# print(os.path.abspath("."))
# print(os.path.curdir)
# file_path = os.path.join(absolute_path, "text_file.txt")
# print(file_path)
# print(os.path.join(absolute_path, "Exam_Preparation", "april_2023.py"))
# print(os.path.join(absolute_path, "Error_Handling_Homework", "email_validator.py"))
# print(os.path.abspath(__file__))
#
# ### Python find abspath to Root Directory #####
# print(os.path.dirname(os.path.abspath(__file__)))
# file_path = os.path.join(absolute_path, "text_file.txt")
# print(file_path)
# print(os.path.isfile('text_file.txt'))


### File Modes

# 'r' - read
# "w" - write but delete all content existing before
# "a" - append to already existing
# "x" - create new file and opens it
# "t" - text mode
# "b" - binary mode
# "+" - reading and writing
