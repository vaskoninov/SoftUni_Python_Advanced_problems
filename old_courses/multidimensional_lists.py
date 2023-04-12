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

n, m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

result = [sum(i) for i in matrix]
print(sum(result))
