# Words Sorting
#
# def words_sorting(*args):
#     words = {}
#
#     for word in args:
#         words[word] = sum([ord(x) for x in word])
#
#     value = sum(words.values())
#
#     if value % 2 != 0:
#         result = {key: value for key, value in sorted(words.items(), key=lambda x: -x[1])}
#     else:
#         result = {key: value for key, value in sorted(words.items(), key=lambda x: x[0])}
#
#     final = []
#
#     for k, v in result.items():
#         final.append(f"{k} - {v}")
#
#     return "\n".join(final)
#
#
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#     ))
#
# # print(
# #     words_sorting(
# #         'escape',
# #         'charm',
# #         'eye'
# #     ))
#
# # print(
# #     words_sorting(
# #         'escape',
# #         'charm',
# #         'mythology'
# #     ))


# Pawn Wars 4

# SIZE = 8

# board = []
# positions = [[], []]


# def save_positions(search_for, index_to_save, r):
#     if search_for in board[r]:
#         positions[index_to_save].append(r)
#         positions[index_to_save].append(board[r].index(search_for))


# for row in range(SIZE):
#     board.append(input().split())  # - - - - - b - => [-, -, -, -, -, b, -]

#     save_positions("w", 0, row)
#     save_positions("b", 1, row)

# if abs(positions[0][1] - positions[1][1]) != 1 or positions[1][0] > positions[0][0]:
#     if SIZE - positions[0][0] - 1 <= positions[1][0]:
#         print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
#     else:
#         print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
# else:
#     place = (positions[0][0] + positions[1][0]) // 2

#     if positions[0][0] % 2 == positions[1][0] % 2:
#         print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
#     else:
#         print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")


# The Martian Rover


# def move_rover(rover, mars, direction, movements):
#     machine = [rover[0] + movements[direction][0], rover[1] + movements[direction][1]]
#     if machine[0] == len(mars):
#         machine[0] = 0
#     if machine[0] < 0:
#         machine[0] = len(mars) - 1
#     if machine[1] < 0:
#         machine[1] = len(mars[0]) - 1
#     if machine[1] == len(mars[0]):
#         machine[1] = 0
#     return machine


# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }

# shorts = {
#     "W": "Water",
#     "M": "Metal",
#     "C": "Concrete",
# }


# resources = {
#     "W": 0,
#     "M": 0,
#     "C": 0,
# }

# rover = []
# mars = []
# for i in range(6):
#     mars.append(input().split())
#     if "E" in mars[i]:
#         rover = [i, mars[i].index("E")]

# directions = input().split(", ")


# for direction in directions:
#     rover = move_rover(rover, mars, direction, movements)
#     if mars[rover[0]][rover[1]] in resources:
#         resources[mars[rover[0]][rover[1]]] += 1
#         print(f"{shorts[mars[rover[0]][rover[1]]]} deposit found at ({rover[0]}, {rover[1]})")

#     if mars[rover[0]][rover[1]] == "R":
#         print(f"Rover got broken at ({rover[0]}, {rover[1]})")
#         break

# if resources["W"] and resources["M"] and resources["C"]:
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")


###### Ramen Shop

from collections import deque

bowls = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while bowls and customers:
    if bowls[-1] == customers[0]:
        bowls.pop()
        customers.popleft()

    elif bowls[-1] > customers[0]:
        bowls[-1] -= customers.popleft()

    elif bowls[-1] < customers[0]:
        customers[0] -= bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(map(str, customers))}")
