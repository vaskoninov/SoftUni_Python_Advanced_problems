# ### Christmas Elves
#
# from collections import deque
#
# elves = deque([int(x) for x in input().split()])
# materials = deque([int(x) for x in input().split()])
#
# energy_used = 0
# toys = 0
# counter = 0
#
# while elves and materials:
#     elf = elves.popleft()
#     if elf < 5:
#         continue
#     counter += 1
#     material = materials.pop()
#
#     if counter % 3 == 0:
#         if elf >= material * 2:
#             if counter % 5 != 0:
#                 toys += 2
#                 elf -= material * 2 - 1
#             else:
#                 elf -= material * 2
#             energy_used += material * 2
#             elves.append(elf)
#         else:
#             materials.append(material)
#             elf *= 2
#             elves.append(elf)
#     else:
#         if elf >= material:
#             if counter % 5 != 0:
#                 toys += 1
#                 elf -= material - 1
#             else:
#                 elf -= material
#             energy_used += material
#             elves.append(elf)
#
#         else:
#             materials.append(material)
#             elf *= 2
#             elves.append(elf)
#
# print(f"Toys: {toys}")
# print(f"Energy: {energy_used}")
# if elves:
#     print(f"Elves left: {', '.join([str(x) for x in elves])}")
# if materials:
#     print(f"Boxes left: {', '.join([str(x) for x in materials])}")

#### Nothpole Challenge

# def give_santa(santa, workshop, direction, movements):
#     clouse = [santa[0] + movements[direction][0], santa[1] + movements[direction][1]]
#     if clouse[0] == len(workshop):
#         clouse[0] = 0
#     if clouse[0] < 0:
#         clouse[0] = len(workshop) - 1
#     if clouse[1] < 0:
#         clouse[1] = len(workshop[0]) - 1
#     if clouse[1] == len(workshop[0]):
#         clouse[1] = 0
#     return clouse
#
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# items = {
#     "D": 0,
#     "G": 0,
#     "C": 0,
# }
# collected = {
#     "D": 0,
#     "G": 0,
#     "C": 0,
# }
#
# total_items = sum(items.values())
#
# rows, cols = [int(x) for x in input().split(", ")]
# workshop = []
# santa = []
#
# for row in range(rows):
#     line = input().split()
#     workshop.append(line)
#     if "Y" in line:
#         santa = [row, line.index("Y")]
#     for key in items:
#         items[key] += line.count(key)
# total_items = sum(items.values())
#
# while True and total_items:
#     command = input()
#     if command == "End":
#         break
#     command = command.split("-")
#     direction = command[0]
#     steps = int(command[1])
#
#     for step in range(steps):
#         workshop[santa[0]][santa[1]] = "x"
#         santa = give_santa(santa, workshop, direction, movements)
#         symbol = workshop[santa[0]][santa[1]]
#         if symbol in collected:
#             collected[symbol] += 1
#             total_items -= 1
#         workshop[santa[0]][santa[1]] = "Y"
#         if total_items == 0:
#             print("Merry Christmas!")
#             break
#
# print("You've collected:")
# print(f"- {collected['D']} Christmas decorations")
# print(f"- {collected['G']} Gifts")
# print(f"- {collected['C']} Cookies")
# for row in workshop:
#     print(*row)


#### Naughty or Nice
from collections import Counter


def naughty_or_nice_list(sequence, *args, **kwargs):
    kids = {}
    result = {
        "Nice": [],
        "Naughty": [],
        "Not found": [],
    }

    for num, kid in sequence:
        if num not in kids:
            kids[num] = []
        kids[num].append(kid)
    print(kids)
    commands = [arg.split('-') for arg in args]

    for command in commands:
        x = int(command[0])
        disc = command[1]
        if x in kids:
            if len(kids[int(x)]) == 1:
                name = kids[x][0]
                result[disc].append(name)
                sequence.remove((x, name))

    counter = Counter(arg[1] for arg in sequence)
    for key, value in kwargs.items():
        if counter[key] == 1:
            result[value].append(key)
            for i, v in enumerate(sequence):
                if v[1] == key:
                    sequence.pop(i)

    for num, kid in sequence:
        # if kid not in result["Naughty"] and kid not in result["Nice"]:
        result["Not found"].append(kid)

    final = []
    for key, value in result.items():
        if value:
            final.append(f"{key}: {', '.join(value)}")
    return "\n".join(final)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
