#### Diagonals

# matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

# primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
# secondary_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

### Diagonal Difference

# def diagonal_difference_sq_matrix(matrix):
#     primary = 0
#     secondary = 0
#     for i in range(len(matrix)):
#         primary += matrix[i][i]
#         secondary += matrix[i][len(matrix) - i - 1]
    
#     return abs(primary - secondary)

# matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

# print(diagonal_difference_sq_matrix(matrix))

### 2x2 Squares in Matrix

# rows, cols = [int(x) for x in input().split()]

# matrix = [input().split() for _ in range(rows)]

# counter = 0

# for row in range(rows - 1):
#     for col in range(cols - 1):
#         if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
#             counter += 1

# print(counter)

### Maximal Sum

# final_result = float('-inf')
# rows, cols = [int(x) for x in input().split()]
# start_row = 0
# start_col = 0
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]

# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_result = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + \
#                          matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + \
#                          matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
#         if current_result > final_result:
#             final_result = current_result
#             start_row = row
#             start_col = col

# print(f"Sum = {final_result}")
# print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
# print(
#     f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}")
# print(
#     f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}")


##### Matrix of Palindromes

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# rows, cols = [int(x) for x in input().split()]

# matrix = []

# for i in range(rows):
#     ll = []
#     for j in range(i, cols + i, 1):
#         ll.append(f"{alphabet[i]}{alphabet[j]}{alphabet[i]}")
#     matrix.append(ll)

# for i in matrix:
#     print(" ".join(i))

##### Matrix Shuffling
# def is_valid(args):
#     if args[0] in range(rows) and args[2] in range(rows) \
#     and args[1] in range(cols) and args[3] in range(cols):
#         return True


# def check_data(args):
#     data = [x.isdigit() for x in args]
#     return all(data)


# def check_value(args):
#     for i in args:
#         if i < 0:
#             return False
#     return True

# rows, cols = [int(x) for x in input().split()]

# matrix = [[x for x in input().split()] for _ in range(rows)]


# while True:
#     command, *data = input().split()
#     if command == "END":
#         break
#     if command == "swap":
#         if len(data) == 4 and check_data(data):
#             data = [int(x) for x in data]
#             if check_value(data) and is_valid(data):
#                 matrix[data[0]][data[1]], matrix[data[2]][data[3]] = \
#                 matrix[data[2]][data[3]], matrix[data[0]][data[1]]
#                 for row in matrix:
#                     print(*row)
#             else:
#                 print("Invalid input!")
#                 continue
#         else:
#             print("Invalid input!")
#             continue
#     else:
#         print("Invalid input!")

#### Snake Moves

# from collections import deque

# rows, cols = [int(x) for x in input().split()]

# line = deque([x for x in input()])

# matrix = []

# for row in range(rows):
#     temp_row = []
#     for col in range(cols):
#         char = line.popleft()
#         temp_row.append(char)
#         line.append(char)
#     if row % 2 != 0:
#         temp_row.reverse()
#     matrix.append(temp_row)

# for row in matrix:
#     print("".join(row))

#### Bombs

# def is_valid(n, m):
#     if n in range(size) and m in range(size):
#         return True


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

# size = int(input())
# bombs = []
# matrix = []

# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])

# coordinates = input().split()

# for coor in coordinates:
#     row, col = [int(x) for x in coor.split(",")]
#     bombs.append((row, col))

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

#         matrix[row][col] = 0

# active_cells = 0
# total_sum = 0
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] > 0:
#             active_cells += 1
#             total_sum += matrix[i][j]

# print(f"Alive cells: {active_cells}")
# print(f"Sum: {total_sum}")
# for row in matrix:
#     print(*row)

#####  Miner


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


####### Radioactive Mutate Vampire Bunnies

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
is_alive = True

is_out = False

for i, v in enumerate(directions):
    if not is_alive or is_out:
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
            is_alive = False
    else:
        is_out = True

    for bunny in bunnies:
        for move in movements:
            to_move = (bunny[0] + movements[move][0], bunny[1] + movements[move][1])
            if is_valid(to_move[0], to_move[1]):
                lair[to_move[0]][to_move[1]] = "B"
                new_bunnies.append((to_move[0], to_move[1]))
                if lair[player_position[0]][player_position[1]] == "B":
                    is_alive = False

    bunnies.extend(new_bunnies)


for row in lair:
    print("".join(row))
if is_out:
    print(f"won: {player_position[0]} {player_position[1]}")
else:
    print(f"dead: {player_position[0]} {player_position[1]}")
