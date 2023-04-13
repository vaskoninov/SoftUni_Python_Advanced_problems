# Multidimensional lists
# lists within lists
# Grid - two-dimensional lists
# Cube = three-dimensional lists

# ll = [1, 2, 3, 4, 5, 6, 7]
#
# mm = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# mm.append([-11])
# print(mm)
# mm.pop()
# print(mm)
#
# print(mm[0][0])

# Cube
#
# cc = [
#     [
#         [1, 2, 3],
#         [2, 3, 4],
#         [4, 5, 6],
#     ],
#     [
#         [6, 7, 8],
#         [7, 8, 9],
#         [10, 11, 12],
#     ],
#     [
#         [13, 14, 15],
#         [16, 17, 18],
#         [19, 20, 21]
#     ]
# ]
#
# print(cc[0][1][2])
#
# matrix = []
#
# for i in range(3):
#     matrix.append([])
#     for j in range(3):
#         matrix[i].append(j)
#
# print(matrix)
# n = 3
# matrix: list[list[int]] = [[x for x in range(n)] for x in range(n)]
# print(matrix)
#

###############

# n, m = [int(x) for x in input().split(', ')]
#
# matrix = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split(', ')]
#     matrix.append(row)
#
# result = [sum(i) for i in matrix]
# print(sum(result))
# print(matrix)

################

# Nested Comprehensions

# -> Creating
# -> Flattening list
# mm = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# new_mm = [v for row in mm for v in row]
# print(new_mm)

###############
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(", ")])
#
# new_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
# print(new_matrix)

##################

# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(", ")])
#
# flatten = [x for row in matrix for x in row]
# print(flatten)

###################

# n, m = [int(x) for x in input().split(', ')]
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# sums = []
# for i in range(len(matrix[0])):
#     sums.append(0)
#     for j in range(len(matrix)):
#         sums[i] += matrix[j][i]
#
# for i in sums:
#     print(i)

####################

# Primary Diagonal (from top left to bottom right( and Secondary Diagonal (from top right to bottom left)
# a value is on PD if row_index == column_index
# a value is on SD if row_index == n - column_index - 1
# Below PD - column_index < row_index
# Above PD - column_index > row_index
#
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# result = 0
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if i == j:
#             result += matrix[i][j]
#
# print(result)

######################
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append(list(input()))
#
# symbol = input()
# location = ()
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         if matrix[row][col] == symbol:
#             if not location:
#                 location = (row, col)
#
# if location:
#     print(location)
# else:
#     print(f"{symbol} does not occur in the matrix")

##################
final_result = 0
rows, cols = [int(x) for x in input().split(', ')]
final_table = []
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

for k in range(rows - 1):
    for l in range(cols - 1):
        result = 0
        table = []
        for i in range(2):
            for j in range(2):
                result += matrix[i + k][j + l]
                table.append(matrix[i + k][j + l])
        if result > final_result:
            final_result = result
            final_table = table

print(*final_table[:2])
print(*final_table[2:])
print(final_result)
