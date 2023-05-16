### Sum Matrix Elements
# rows, cols = [int(x) for x in input().split(", ")]
#
# matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
#
# result = sum((sum(row) for row in matrix))
#
# print(result)
# print(matrix)

### Even Matrix

# matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))]
#
# print(matrix)

### Flattening Matrix

# matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]
# flattened_matrix = [x for row in matrix for x in row]
# print(flattened_matrix)

### Sum Matrix Columns

# rows, cols = [int(x) for x in input().split(", ")]
# sums = [0] * cols
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# for row in range(rows):
#     for col in range(cols):
#         sums[col] += matrix[row][col]
#
# print(*sums, sep="\n")

### Primary Diagonal

# size = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(size)]
# result = 0
# for n in range(size):
#     result += matrix[n][n]
# print(result)


### Symbol in Matrix
#
# size = int(input())
# matrix = [input() for _ in range(size)]
#
# symbol = input()
# found = False
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == symbol:
#             print(f"({i}, {j})")
#             found = True
#             break
#     if found:
#         break
# else:
#     print(f"{symbol} does not occur in the matrix")

#### Square with Maximum Sum

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
