###### Climb the Peaks

# from collections import deque
#
# food = deque([int(x) for x in input().split(", ")])
# stamina = deque([int(x) for x in input().split(", ")])
#
# peaks = deque([
#     ("Vihren", 80),
#     ("Kutelo", 90),
#     ("Banski Suhodol", 100),
#     ("Polezhan", 60),
#     ("Kamenitza", 70)
# ])
#
# days = 7
# conquered = []
#
# for i in range(days):
#     portion = food.pop()
#     strength = stamina.popleft()
#     peak_info = peaks.popleft()
#     if portion + strength >= peak_info[1]:
#         conquered.append(peak_info[0])
#         if len(conquered) == 5:
#             break
#     else:
#         peaks.appendleft(peak_info)
#
# if len(conquered) == 5:
#     print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
# else:
#     print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
# if conquered:
#     print("Conquered peaks:")
#     print("\n".join(conquered))


####### Navy Battle
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# size = int(input())
# battlefield = []
# sub = ()
# hits = 0
# ships = 3
#
# for i in range(size):
#     battlefield.append(list(input()))
#     if "S" in battlefield[i]:
#         sub = (i, battlefield[i].index("S"))
#
# while True:
#     command = input()
#     battlefield[sub[0]][sub[1]] = "-"
#     sub = (sub[0] + movements[command][0], sub[1] + movements[command][1])
#     if battlefield[sub[0]][sub[1]] == "-":
#         battlefield[sub[0]][sub[1]] = 'S'
#         continue
#     if battlefield[sub[0]][sub[1]] == "*":
#         hits += 1
#         battlefield[sub[0]][sub[1]] = "S"
#         if hits == 3:
#             print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub[0]}, {sub[1]}]!")
#             break
#     if battlefield[sub[0]][sub[1]] == "C":
#         battlefield[sub[0]][sub[1]] = "S"
#         ships -= 1
#         if ships == 0:
#             print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#             break
#
# for row in battlefield:
#     print("".join(row))

###### Student Credits

def students_credits(*args):
    courses = {}
    final_credits = 0
    for entry in args:
        course, credits_per_course, max_points, d_points = entry.split("-")
        d_credits = (int(d_points) / int(max_points)) * int(credits_per_course)
        courses[course] = d_credits
        final_credits += d_credits

    result = []

    if final_credits >= 240:
        result.append(f"Diyan gets a diploma with {final_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - final_credits):.1f} credits more for a diploma.")

    for key, value in sorted(courses.items(), key=lambda x: -x[1]):
        result.append(f"{key} - {value:.1f}")

    return "\n".join(result)


# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
