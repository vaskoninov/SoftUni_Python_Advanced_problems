##### Temple of Doom

# from collections import deque
#
# tools = deque([int(x) for x in input().split()])
# substances = deque([int(x) for x in input().split()])
# challenges = [int(x) for x in input().split()]
#
# while tools and substances:
#     tool = tools.popleft()
#     substance = substances.pop()
#
#     value = tool * substance
#
#     if value in challenges:
#         challenges.remove(value)
#         if not challenges:
#             print("Harry found an ostracon, which is dated to the 6th century BCE.")
#             break
#
#     else:
#         tool += 1
#         tools.append(tool)
#         substance -= 1
#         if substance > 0:
#             substances.append(substance)
#         if not substances:
#             print("Harry is lost in the temple. Oblivion awaits him.")
#             break
# if tools:
#     print(f"Tools: {', '.join([str(x) for x in tools])}")
# if substances:
#     print(f"Substances: {', '.join([str(x) for x in substances])}")
# if challenges:
#     print(f"Challenges: {', '.join([str(x) for x in challenges])}")


##### Mouse in the Kitchen

# def is_valid(n, m):
#     return n in range(rows) and m in range(cols)
#
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# rows, cols = [int(x) for x in input().split(",")]
#
# area = []
# mouse = ()
# cheese = 0
#
# for row in range(rows):
#     area.append(list(input()))
#     if "M" in area[row]:
#         mouse = (row, area[row].index("M"))
#     cheese += area[row].count("C")
#
# while True:
#     command = input()
#     if command == "danger":
#         print("Mouse will come back later!")
#         break
#     to_move = (mouse[0] + movements[command][0], mouse[1] + movements[command][1])
#     if is_valid(to_move[0], to_move[1]):
#         if area[to_move[0]][to_move[1]] == "@":
#             continue
#         else:
#             area[mouse[0]][mouse[1]] = "*"
#             mouse = (to_move[0], to_move[1])
#             if area[mouse[0]][mouse[1]] == "C":
#                 area[mouse[0]][mouse[1]] = "M"
#                 cheese -= 1
#                 if cheese == 0:
#                     print("Happy mouse! All the cheese is eaten, good night!")
#                     break
#             if area[mouse[0]][mouse[1]] == "T":
#                 area[mouse[0]][mouse[1]] = "M"
#                 print("Mouse is trapped!")
#                 break
#             if area[mouse[0]][mouse[1]] == "*":
#                 area[mouse[0]][mouse[1]] = "M"
#     else:
#         print("No more cheese for tonight!")
#         break
#
# for row in area:
#     print(f"{''.join(row)}")


#### Enrollment

def gather_credits(credits, *args):
    needed_credits = credits
    courses = {}
    result = []
    if needed_credits > 0:
        for course, value in args:
            if course not in courses:
                courses[course] = value
            if sum(courses.values()) >= needed_credits:
                break

    achieved_credits = sum(courses.values())
    if achieved_credits >= needed_credits:
        result.append(f"Enrollment finished! Maximum credits: {achieved_credits}.")
        result.append(f"Courses: {', '.join(sorted(courses.keys()))}")

        return "\n".join(result)
    else:
        return f"You need to enroll in more courses! You have to gather {needed_credits - achieved_credits} credits more."

# print(gather_credits(
#     0,
#     ("Basics", 20)
# ))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
#
# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
#
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
