# test = """3 4
# A B B D
# E B B B
# I J B B
# """
# sys.stdin = StringIO(test)

# n = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
#
# p_d = [matrix[i][i] for i in range(n)]
# s_d = [matrix[n - i - 1][i] for i in range(n - 1, -1, -1)]
#
# print(f"Primary diagonal: {', '.join(map(str, p_d))}. Sum: {sum(p_d)}")
# print(f"Secondary diagonal: {', '.join(map(str, s_d))}. Sum: {sum(s_d)}")
###################
# n = int(input())
#
# matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]
#
# p_d = sum([matrix[i][i] for i in range(n)])
# s_d = sum([matrix[n - i - 1][i] for i in range(n - 1, -1, -1)])
#
# difference = abs(p_d - s_d)
# print(difference)

##########
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [input().split() for _ in range(rows)]
#
# counter = 0
#
# for row in range(rows - 1):
#     for col in range(cols - 1):
#         if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
#             counter += 1
#
# print(counter)

################
# final_result = float('-inf')
# rows, cols = [int(x) for x in input().split()]
# start_row = 0
# start_col = 0
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_result = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + \
#                          matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + \
#                          matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
#         if current_result > final_result:
#             final_result = current_result
#             start_row = row
#             start_col = col
#
# print(f"Sum = {final_result}")
# print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
# print(
#     f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}")
# print(
#     f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}")
#
# final_result = float('-inf')
# rows, cols = [int(x) for x in input().split()]
# final_table = []
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         result = 0
#         table = []
#         for i in range(3):
#             for j in range(3):
#                 result += matrix[i + row][col + j]
#                 table.append(matrix[i + row][col + j])
#         if result > final_result:
#             final_result = result
#             final_table = table
#
# print(f"Sum = {final_result}")
# print(*final_table[:3])
# print(*final_table[3:6])
# print(*final_table[6:])

#######################

# alphabet = string.ascii_lowercase #not recognized by judge
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for i in range(rows):
#     ll = []
#     for j in range(i, cols + i, 1):
#         ll.append(f"{alphabet[i]}{alphabet[j]}{alphabet[i]}")
#     matrix.append(ll)
#
# for i in matrix:
#     print(" ".join(i))

####################

# def valid_row(n):
#     return n in range(rows)
#
#
# def valid_col(n):
#     return n in range(cols)
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = []
# for _ in range(rows):
#     matrix.append(input().split())
#
# while True:
#     instructions = input()
#     if instructions == "END":
#         break
#     instructions = instructions.split()
#     command = instructions[0]
#     if command == "swap":
#         string_check = [x.isdigit() for x in instructions[1:]]
#         if not all(string_check):
#             print('Invalid input!')
#             continue
#         check = [int(x) >= 0 for x in instructions[1:]]
#         if not all(check):
#             print('Invalid input!')
#             continue
#         coordinates = [int(x) for x in instructions[1:]]
#         if len(coordinates) != 4:
#             print('Invalid input!')
#             continue
#         row1 = coordinates[0]
#         col1 = coordinates[1]
#         row2 = coordinates[2]
#         col2 = coordinates[3]
#         if valid_row(row1) and valid_row(row2) and valid_col(col1) and valid_col(col1):
#             matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#             for row in matrix:
#                 print(*row)
#         else:
#             print('Invalid input!')
#     else:
#         print('Invalid input!')


########################
#
# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
#
# line = deque([x for x in input()])
#
# matrix = []
#
# for i in range(rows):
#
#     if i % 2 == 0:
#         ll = []
#         for j in range(cols):
#             char = line.popleft()
#             ll.append(char)
#             line.append(char)
#     else:
#         ll = []
#         for k in range(cols - 1, -1, -1):
#             rach = line.popleft()
#             ll.append(rach)
#             line.append(rach)
#         ll = reversed(ll)
#     matrix.append(ll)
#
# for row in matrix:
#     print("".join(row))
