##### Words Sorting
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


####### Pawn Wars 4

SIZE = 8

board = []
positions = [[], []]


def save_positions(search_for, index_to_save, r):
    if search_for in board[r]:
        positions[index_to_save].append(r)
        positions[index_to_save].append(board[r].index(search_for))


for row in range(SIZE):
    board.append(input().split())
    save_positions("w", 0, row)
    save_positions("b", 1, row)

if abs(positions[0][1] - positions[1][1]) != 1 or positions[1][0] > positions[0][0]:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print("Black")
    else:
        print("white")
else:
    place = (positions[0][0] + positions[1][0]) // 2

    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Black on {chr(97 + positions[0][1])}{SIZE - place}")
    else:
        print(f"white on {chr(97 + positions[1][1])}{SIZE - place}")
