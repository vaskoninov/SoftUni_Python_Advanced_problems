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
