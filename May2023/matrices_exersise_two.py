#### Flatten List

# matrix = [[int(x) for x in row.split()] for row in input().split("|")]

# matrix.reverse()

# flatten = [x for row in matrix for x in row]

# print(*flatten)

#### Matrix Modification

# def is_valid(n, m):
#     return n in range(size) and m in range(size)


# size = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(size)]

# while True:
#     instructions = input()
#     if instructions == "END":
#         for row in matrix:
#             print(*row)
#         break
#     instructions = instructions.split()
#     command = instructions[0]
#     row = int(instructions[1])
#     col = int(instructions[2])
#     value = int(instructions[3])

#     if is_valid(row, col):
#         if command == "Add":
#             matrix[row][col] += value
#         if command == "Subtract":
#             matrix[row][col] -= value
#     else:
#         print("Invalid coordinates")

##### Knight Game

# def is_valid(n, m):
#     return n in range(size) and m in range(size)



# knights_removed = 0
# captured_pieces = 0
# to_move = ()

# movements = {
#     "up_left": (-2, -1),
#     "up_right": (-2, 1),
#     "right_up": (-1, -2),
#     "right_down": (1, -2),
#     "left_up": (-1, 2),
#     "left_down": (1, 2),
#     "down_left": (2, -1),
#     "down_right": (2, 1),
# }

# available_knights = {}

# size = int(input())

# matrix = [[x for x in input()] for _ in range(size)]

# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == "K":
#             available_knights[(i, j)] = 0


# while True:
#     for knight in available_knights:
#         available_knights[knight] = 0
#         for move, value in movements.items():
#             to_move = (knight[0] + value[0], knight[1] + value[1])
#             if is_valid(to_move[0], to_move[1]):
#                 if matrix[to_move[0]][to_move[1]] == "K":
#                     available_knights[knight] += 1
#             else:
#                 continue

#     check = [x == 0 for x in available_knights.values()]
#     if all(check):
#         break
#     else:
#         value_to_delete = max(available_knights.values())
#         for key, value in available_knights.items():
#             if value == value_to_delete:
#                 knights_removed += 1
#                 matrix[key[0]][key[1]] = 0
#                 del available_knights[key]
#                 break

# print(knights_removed)

####### Easter Bunny