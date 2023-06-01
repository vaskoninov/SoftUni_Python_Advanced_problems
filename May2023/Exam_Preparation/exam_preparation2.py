### Flowers Finder

# from collections import deque

# vowels = deque(input().split())
# consonants = deque(input().split())
# word_found = False


# flowers = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil",
# }

# while vowels and consonants and not word_found:
#     vowel = vowels.popleft()
#     consonant = consonants.pop()

#     for word in flowers:
#         flowers[word] = flowers[word].replace(vowel, "")
#         flowers[word] = flowers[word].replace(consonant, "")
#         if flowers[word] == "":
#             word_found = True
#             print(f"Word found: {word}")
#             break


# if not word_found:
#     print("Cannot find any word!")

# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")


###### Pawn Wars
# def check_if_can_capture(coordinates_attacker, coordinates_defender):
#     row_a = coordinates_attacker[0]
#     col_a = coordinates_attacker[1]
#     row_d = coordinates_defender[0]
#     col_d = coordinates_defender[1]
#     if row_a - 1 >= 0 and col_a - 1 >= 0:
#         if row_a - 1 == row_d and col_a - 1 == col_d:
#             return [row_a - 1, col_a - 1]
#     if row_a - 1 >= 0 and col_a + 1 < 8:
#         if row_a - 1 == row_d and col_a + 1 == col_d:
#             return [row_a - 1, col_a + 1]
#     if row_a + 1 < 8 and col_a - 1 >= 0:
#         if row_a + 1 == row_d and col_a - 1 == col_d:
#             return [row_a + 1, col_a - 1]
#     if row_a + 1 < 8 and col_a + 1 < 8:
#         if row_a + 1 == row_d and col_a + 1 == col_d:
#             return [row_a + 1, col_a + 1]
#
#
# matrix = []
# for _ in range(8):
#     matrix.append(input().split())
#
# white_pawn_coordinates = []
# black_pawn_coordinates = []
#
# position_row = {
#     0: "8",
#     1: "7",
#     2: "6",
#     3: "5",
#     4: "4",
#     5: "3",
#     6: "2",
#     7: "1",
# }
# positions_col = {
#     0: "a",
#     1: "b",
#     2: "c",
#     3: "d",
#     4: "e",
#     5: "f",
#     6: "g",
#     7: "h",
# }
#
# for row in range(8):
#     for col in range(8):
#         if matrix[row][col] == "w":
#             white_pawn_coordinates = [row, col]
#         if matrix[row][col] == "b":
#             black_pawn_coordinates = [row, col]
#
# for _ in range(8):
#     capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
#     if capture_on:
#         position = positions_col[capture_on[1]] + position_row[capture_on[0]]
#         print(f"Game over! White win, capture on {position}.")
#         break
#
#     white_pawn_coordinates[0] -= 1
#
#     if white_pawn_coordinates[0] == 0:
#         position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
#         print(f"Game over! White pawn is promoted to a queen at {position}.")
#         break
#
#     capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
#     if capture_on:
#         position = positions_col[capture_on[1]] + position_row[capture_on[0]]
#         print(f"Game over! Black win, capture on {position}.")
#         break
#
#     black_pawn_coordinates[0] += 1
#
#     if black_pawn_coordinates[0] == 7:
#         position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
#         print(f"Game over! Black pawn is promoted to a queen at {position}.")
#         break

###### Springtime

# def start_spring(**kwargs):
#     collections = {}
#     result = []
#     for key, value in kwargs.items():
#         if value not in collections:
#             collections[value] = []
#         collections[value].append(key)
#
#     collections = {key: sorted(value) for key, value \
#                    in sorted(collections.items(), key=lambda x: (-len(x[1]), x[0]))}
#
#     for kind, things in collections.items():
#         result.append(f"{kind}:")
#         for t in things:
#             result.append(f"-{t}")
#     return "\n".join(result)


#
# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
# print(start_spring(**example_objects))
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))

#### Flower Finder 2
# from collections import deque
#
# vowels = deque(input().split())
# consonants = deque(input().split())
#
# flowers = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil",
# }
#
# flower_found = False
#
# while vowels and consonants and not flower_found:
#     letters = [vowels.popleft(), consonants.pop()]
#
#     for flower in flowers:
#         flowers[flower] = flowers[flower].replace(letters[0], "")
#         flowers[flower] = flowers[flower].replace(letters[1], "")
#         if flowers[flower] == "":
#             print(f"Word found: {flower}")
#             flower_found = True
#             break
#
# if not flower_found:
#     print("Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")


##### Flower Finder 3
#
# from collections import deque
#
# vowels = deque(input().split())
# consonants = deque(input().split())
# flowers_list = ["rose", "tulip", "lotus", "daffodil"]
#
# flowers = {}
#
# for flower in flowers_list:
#     flowers[flower] = ["*"] * len(flower)
#
# flower_found = False
#
# while vowels and consonants and not flower_found:
#     letters = [vowels.popleft(), consonants.pop()]
#
#     for flower in flowers:
#         for i, char in enumerate(flower):
#             if char in letters:
#                 flowers[flower][i] = char
#                 if flower == ''.join(flowers[flower]):
#                     print(f"Word found: {flower}")
#                     flower_found = True
#                     break
#
# if not flower_found:
#     print("Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")

###### Pawn Wars 2
def is_valid(n, m):
    return n in range(8) and m in range(8)


letters = "abcdefgh"
nums = "87654321"

w = []
b = []
field = []

for row in range(8):
    field.append(input().split())
    if "w" in field[row]:
        w = [row, field[row].index("w")]
    if "b" in field[row]:
        b = [row, field[row].index("b")]

for _ in range(8):
    field[w[0]][w[1]] = "-"
    if is_valid(w[0] - 1, w[1] - 1):
        if field[w[0] - 1][w[1] - 1] == "b":
            print(f"Game over! White win, capture on {letters[w[1] - 1]}{nums[w[0] - 1]}.")
            break
    if is_valid(w[0] - 1, w[1] + 1):
        if field[w[0] - 1][w[1] + 1] == "b":
            print(f"Game over! White win, capture on {letters[w[1] + 1]}{nums[w[0] - 1]}.")
            break
    w[0] -= 1
    field[w[0]][w[1]] = "w"
    if w[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {letters[w[1]]}{nums[w[0]]}.")
        break

    field[b[0]][b[1]] = "-"
    if is_valid(b[0] + 1, b[1] - 1):
        if field[b[0] + 1][b[1] - 1] == "w":
            print(f"Game over! Black win, capture on {letters[b[1] - 1]}{nums[b[0] + 1]}.")
            break
    if is_valid(b[0] + 1, b[1] + 1):
        if field[b[0] + 1][b[1] + 1] == "w":
            print(f"Game over! Black win, capture on {letters[b[1] + 1]}{nums[b[0] + 1]}.")
            break
    b[0] += 1
    field[b[0]][b[1]] = "b"
    if b[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {letters[b[1]]}{nums[b[0]]}.")
        break
