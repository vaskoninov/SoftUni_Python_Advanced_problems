# matrix = [[int(x) for x in row.split()] for row in input().split("|")]

# matrix.reverse()

# flatten = [x for row in matrix for x in row]

# print(*flatten)

######################


# def is_valid(n, m):
#     return n in range(size) and m in range(size)


# size = int(input())
# matrix = []

# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])

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

#####################
# def is_valid(n, m):
#     return n in range(size) and m in range(size)
#
#
# matrix = []
# knights_removed = 0
# captured_pieces = 0
# to_move = ()
#
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
#
# available_knights = {}
#
# size = int(input())
#
# for _ in range(size):
#     matrix.append(list(input()))
#
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == "K":
#             available_knights[(i, j)] = 0
#
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
#
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
#
# print(knights_removed)

###################

# def is_valid(n, m):
#     return n in range(size) and m in range(size)
#
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# size = int(input())
#
# field = []
#
# harvest = {
#     "right": {
#         "cells": [],
#         "total": 0,
#     },
#     "left": {
#         "cells": [],
#         "total": 0,
#     },
#     "up": {
#         "cells": [],
#         "total": 0,
#     },
#     "down": {
#         "cells": [],
#         "total": 0,
#     },
# }
#
# for _ in range(size):
#     field.append(input().split())
#
# bunny = ()
#
# for i in range(size):
#     for j in range(size):
#         if field[i][j] == "B":
#             bunny = (i, j)
#
# for direction, coord in movements.items():
#     current_bunny = bunny
#     while True:
#         current_bunny = (current_bunny[0] + coord[0], current_bunny[1] + coord[1])
#         if is_valid(current_bunny[0], current_bunny[1]):
#             if field[current_bunny[0]][current_bunny[1]].isdigit():
#                 harvest[direction]['cells'].append([current_bunny[0], current_bunny[1]])
#                 harvest[direction]['total'] += int(field[current_bunny[0]][current_bunny[1]])
#             else:
#                 break
#         else:
#             break
#
# most_profitable_directions = max(harvest, key=lambda v: harvest[v]['total'])
#
# for key, values in harvest.items():
#     if key == most_profitable_directions:
#         print(key)
#         for item in values['cells']:
#             print(item)
#         print(values['total'])

#################

# def is_valid(n, m):
#     return n in range(size) and m in range(size)
#
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# tea = 0
#
# size = int(input())
# alice = ()
# field = []
#
# for _ in range(size):
#     field.append([int(x) if x.isdigit() else x for x in input().split()])
#
# for i in range(size):
#     for j in range(size):
#         if field[i][j] == "A":
#             alice = (i, j)
#
# while True:
#     command = input()
#     field[alice[0]][alice[1]] = "*"
#     alice = (alice[0] + movements[command][0], alice[1] + movements[command][1])
#     if is_valid(alice[0], alice[1]):
#         if isinstance(field[alice[0]][alice[1]], int):
#             tea += field[alice[0]][alice[1]]
#             if tea >= 10:
#                 field[alice[0]][alice[1]] = "*"
#                 print("She did it! She went to the party.")
#                 break
#         if field[alice[0]][alice[1]] == "R":
#             field[alice[0]][alice[1]] = "*"
#             print("Alice didn't make it to the tea party.")
#             break
#     else:
#         print("Alice didn't make it to the tea party.")
#         break
# for row in field:
#     print(*row)

##############
#
# def is_valid(n, m):
#     return n in range(len(field)) and m in range(len(field[0]))
#
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
# field = []
# shooter = ()
# shot_targets = []
#
# targets = 0
#
# for i in range(5):
#     row = input().split()
#     field.append(row)
#     if "A" in row:
#         shooter = (i, row.index('A'))
#
# n = int(input())
#
# for row in field:
#     for item in row:
#         if item == "x":
#             targets += 1
#
# for i in range(n):
#     commands = input().split()
#     command = commands[0]
#     direction = commands[1]
#     current_shooter = ()
#     if command == "move":
#         steps = int(commands[2])
#         if direction == "right":
#             current_shooter = (shooter[0], shooter[1] + steps)
#         elif direction == "left":
#             current_shooter = (shooter[0], shooter[1] - steps)
#         elif direction == "up":
#             current_shooter = (shooter[0] - steps, shooter[1])
#         elif direction == "down":
#             current_shooter = (shooter[0] + steps, shooter[1])
#
#         if is_valid(current_shooter[0], current_shooter[1]) and \
#                 field[current_shooter[0]][current_shooter[1]] == ".":
#             field[shooter[0]][shooter[1]] = "."
#             shooter = current_shooter
#             field[shooter[0]][shooter[1]] = "A"
#
#     if command == "shoot":
#         shoot_row, shoot_col = shooter
#         for shot in range(5):
#
#             to_shoot = (shoot_row + movements[direction][0], shoot_col + movements[direction][1])
#             if is_valid(to_shoot[0], to_shoot[1]):
#                 if field[to_shoot[0]][to_shoot[1]] == "x":
#                     shot_targets.append([to_shoot[0], to_shoot[1]])
#                     targets -= 1
#                     field[to_shoot[0]][to_shoot[1]] = "."
#                     break
#                 else:
#                     shoot_row, shoot_col = to_shoot[0], to_shoot[1]
#
#     if not targets:
#         break
#
# if targets:
#     print(f"Training not completed! {targets} targets left.")
# else:
#     print(f"Training completed! All {len(shot_targets)} targets hit.")
#
# for target in shot_targets:
#     print(target)
