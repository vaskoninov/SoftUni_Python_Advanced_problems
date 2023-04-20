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
