#### Stewards #####

# from collections import deque
#
# seats = input().split(", ")
# first = deque(int(x) for x in input().split(", "))
# second = deque(int(x) for x in input().split(", "))
#
# matches = []
# rotations = 0
#
# while rotations < 10 and len(matches) < 3:
#     rotations += 1
#     f = first.popleft()
#     s = second.pop()
#     char = chr(f + s)
#
#     combinations = [f"{f}{char}", f"{s}{char}"]
#
#     found = []
#     for seat in seats:
#         if char in seat:
#             found.append(seat)
#     if found:
#         for combination in combinations:
#             if combination in found:
#                 if combination not in matches:
#                     matches.append(combination)
#     else:
#         first.append(f)
#         second.appendleft(s)
# print(f"Seat matches: {', '.join(matches)}")
# print(f"Rotations count: {rotations}")

####### CRUD #########
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# matrix = [[x for x in input().split()] for _ in range(6)]
#
# initial_pos = input().split(", ")
# start = ((int(initial_pos[0][1])), int(initial_pos[1][0]))
#
# while True:
#     commands = input()
#     if commands == "Stop":
#         break
#     commands = commands.split(", ")
#     command = commands[0]
#     direction = commands[1]
#     start = (start[0] + movements[direction][0], start[1] + movements[direction][1])
#     if command == "Create":
#         value = commands[2]
#         if matrix[start[0]][start[1]] == ".":
#             matrix[start[0]][start[1]] = value
#     if command == "Update":
#         value = commands[2]
#         if matrix[start[0]][start[1]] != ".":
#             matrix[start[0]][start[1]] = value
#     if command == "Delete":
#         if matrix[start[0]][start[1]] != ".":
#             matrix[start[0]][start[1]] = "."
#     if command == "Read":
#         if matrix[start[0]][start[1]] != ".":
#             print(matrix[start[0]][start[1]])
# [print(*row) for row in matrix]


##### Song Creator #######

def add_songs(*args):
    songs = {}
    result = []

    for song, lyrics in args:

        if song in songs:
            songs[song].extend(lyrics)
        else:
            songs[song] = lyrics

    for song, lyrics in songs.items():
        result.append(f"- {song}")
        if lyrics:
            result.append("\n".join(lyrics))

    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
