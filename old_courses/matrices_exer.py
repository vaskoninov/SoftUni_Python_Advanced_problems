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
final_result = 0
rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for row in range(rows - 2):
    for col in range(cols - 2):
        result = 0
        for i in range(3):
            for j in range(3):
                result += matrix[i + row][col + j]
        if result > final_result:
            final_result = result

print(final_result)
