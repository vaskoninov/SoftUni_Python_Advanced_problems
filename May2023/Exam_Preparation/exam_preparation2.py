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
def white_capture(w):
    return field[w[0] - 1][w[1] - 1] == "b" or field[w[0] - 1][w[1] + 1] == "b"


def black_capture(b):
    return field[b[0] + 1][b[1] - 1] == "w" or field[b[0] + 1][b[1] + 1] == "w"

field = []
b = []
w = []
letters = "abcdefgh"
numbers = "87654321"

for i in range(8):
    field.append(input().split())
    if "b" in field[i]:
        b = [i, field[i].index("b")]
    if "w" in field[i]:
        w = [i, field[i].index("w")]

while True:
    field[w[0]][w[1]] = "-"
    if white_capture:
        if field[w[0] - 1][w[1] - 1] == "b":
            field[w[0] - 1][w[1] - 1] = "w"
            w = [w[0] - 1, w[1] - 1]
        else:
            field[w[0] - 1][w[1] + 1] = "w"
            w = [w[0] - 1, w[1] + 1]
        print(f"Game over! White win, capture on {letters[w[1]]}{numbers[w[0]]}.")
        break
    
    field[w[0] - 1][w[1]] = "w"
    w = [w[0] - 1, w[1]]

    if w[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {letters[w[1]]}{numbers[w[0]]}.")
        break


    field[b[0]][b[1]] = "-"
    if black_capture:
        if field[b[0] + 1][b[1] - 1] == "w":
            field[b[0] + 1][b[1] - 1] = "b"
            b = [b[0] + 1, b[1] - 1]
        else:
            field[b[0] + 1][b[1] + 1] == "b"
            b = [b[0] + 1, b[1] + 1]
        print(f"Game over! White win, capture on {letters[b[1]]}{numbers[b[0]]}.")
        break

    field[b[0] + 1][w[1]] = "b"
    w = [w[0] + 1, w[1]]

    if b[0] == 7:
        print(f"Game over! White pawn is promoted to a queen at {letters[b[1]]}{numbers[b[0]]}.")
        break