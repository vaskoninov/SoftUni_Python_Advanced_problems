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

###############
# def is_valid(n, m):
#     if n in range(size) and m in range(size):
#         return True
#
#
# movements = {
#     "u_l": (-1, -1),
#     "l": (0, -1),
#     "b_l": (1, -1),
#     "u": (-1, 0),
#     "b": (1, 0),
#     "u_r": (-1, 1),
#     "r": (0, 1),
#     "b_r": (1, 1),
# }
#
# size = int(input())
# bombs = []
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# coordinates = input().split()
#
# for coor in coordinates:
#     row, col = [int(x) for x in coor.split(",")]
#     bombs.append((row, col))
#
# for bomb in bombs:
#     row = bomb[0]
#     col = bomb[1]
#     bomb = matrix[row][col]
#     if bomb > 0:
#         for move in movements:
#             c_row = row + movements[move][0]
#             c_col = col + movements[move][1]
#             if is_valid(c_row, c_col):
#                 if matrix[c_row][c_col] > 0:
#                     matrix[c_row][c_col] -= bomb
#
#         matrix[row][col] = 0
#
# active_cells = 0
# total_sum = 0
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] > 0:
#             active_cells += 1
#             total_sum += matrix[i][j]
#
# print(f"Alive cells: {active_cells}")
# print(f"Sum: {total_sum}")
# for row in matrix:
#     print(*row)

###################
# # from collections import deque
# def is_valid(n, m):
#     if n in range(size) and m in range(size):
#         return True


# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
# matrix = []
# coal_available = 0
# coal_collected = 0
# current_position = ()
# coal_locations = []
# miner_position = ()

# size = int(input())
# commands = input().split()

# for _ in range(size):
#     matrix.append(input().split())
# print(matrix)

# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == "s":
#             miner_position = (i, j)
#         if matrix[i][j] == "c":
#             coal_available += 1
#             coal_locations.append((i, j))

# for i in range(len(commands)):
#     command = commands[i]
#     to_move = (miner_position[0] + movements[command][0], miner_position[1] + movements[command][1])
#     if is_valid(to_move[0], to_move[1]):
#         current_position = matrix[to_move[0]][to_move[1]]
#         if current_position == "c":
#             coal_collected += 1
#             coal_available -= 1
#             coal_locations.remove((to_move[0], to_move[1]))
#             matrix[to_move[0]][to_move[1]] = "*"
#             miner_position = to_move
#             if coal_available == 0:
#                 print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
#                 break
#         elif current_position == "e":
#             miner_position = to_move
#             print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
#             break
#         else:
#             miner_position = to_move
#     else:
#         continue
# else:
#     print(f"{coal_available} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")


##############################
def is_valid(n, m):
    if n in range(rows) and m in range(cols):
        return True


movements = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

rows, cols = [int(x) for x in input().split()]

lair = []

for _ in range(rows):
    lair.append(list(input()))

bunnies = []
player_position = ()

for i in range(len(lair)):
    for j in range(len(lair[0])):
        if lair[i][j] == "B":
            bunnies.append((i, j))
        if lair[i][j] == "P":
            player_position = (i, j)

directions = list(input())
is_alive = False
is_active = True
is_out = False

for i, v in enumerate(directions):
    if not is_active:
        break
    command = v
    new_bunnies = []
    new_player_position = (
        movements[command][0] + player_position[0],
        movements[command][1] + player_position[1],
    )
    lair[player_position[0]][player_position[1]] = "."
    if is_valid(new_player_position[0], new_player_position[1]):
        player_position = new_player_position
        if lair[new_player_position[0]][new_player_position[1]] == ".":
            lair[new_player_position[0]][new_player_position[1]] = "P"
        else:
            is_active = False
    else:
        is_out = True
        is_active = False

    for bunny in bunnies:
        for move in movements:
            to_move = (bunny[0] + movements[move][0], bunny[1] + movements[move][1])
            if is_valid(to_move[0], to_move[1]):
                lair[to_move[0]][to_move[1]] = "B"
                new_bunnies.append((to_move[0], to_move[1]))
                if (
                    lair[bunny[0] + movements[move][0]][bunny[1] + movements[move][1]]
                    == player_position
                ):
                    is_active = False

    bunnies.extend(new_bunnies)


if lair[player_position[0]][player_position[1]] == "P" or is_out:
    is_alive = True

for row in lair:
    print("".join(row))
if is_alive:
    print(f"won: {player_position[0]} {player_position[1]}")
else:
    print(f"dead: {player_position[0]} {player_position[1]}")
