### Rubber Duck
# from collections import deque

# ducks = {
#     "Darth Vader Ducky": 0,
#     "Thor Ducky": 0,
#     "Big Blue Rubber Ducky": 0,
#     "Small Yellow Rubber Ducky": 0,
# }

# programmers = deque([int(x) for x in input().split()])
# tasks = deque([int(x) for x in input().split()])


# while tasks:
#     coder = programmers.popleft()
#     task = tasks.pop()
#     result = coder * task
#     if result > 240:
#         tasks.append(task - 2)
#         programmers.append(coder)
#     elif 0 < result <= 60:
#         ducks["Darth Vader Ducky"] += 1
#     elif 61 < result <= 120:
#         ducks["Thor Ducky"] += 1
#     elif 121 < result <= 180:
#         ducks["Big Blue Rubber Ducky"] += 1
#     elif 181 < result <= 240:
#         ducks["Small Yellow Rubber Ducky"] += 1

# print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
# for key, value in ducks.items():
#     print(f"{key}: {value}")

##### The Squirrel

def is_valid(n, m):
    if n in range(size) and m in range(size):
        return True


movements = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}
nuts = 0

size = int(input())
squirrel = None
directions = [x for x in input().split(", ")]
matrix = []

for i in range(size):
    row = list(input())
    if "s" in row:
        squirrel = (i, row.index("s"))
    matrix.append(row)

for direction in directions:
    to_move = (squirrel[0] + movements[direction][0], squirrel[1] + movements[direction][1])
    if is_valid(to_move[0], to_move[1]):
        matrix[squirrel[0]][squirrel[1]] = "*"
        squirrel = (to_move[0], to_move[1])
        if matrix[to_move[0]][to_move[1]] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            print(f"Hazelnuts collected: {nuts}")
            break
        if matrix[to_move[0]][to_move[1]] == "h":
            nuts += 1
            matrix[to_move[0]][to_move[1]] = "*"
            if nuts == 3 :
                print("Good job! You have collected all hazelnuts!")
                print(f"Hazelnuts collected: {nuts}")
                break
        if matrix[to_move[0]][to_move[1]] == "*":
            continue
    else:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {nuts}")
        break
else:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {nuts}")