##### Numbers #######
#
# set_one = set([int(x) for x in input().split()])
# set_two = set([int(x) for x in input().split()])
#
# n = int(input())
#
# func_mapper = {
#     "Add First": lambda x: [set_one.add(num) for num in x],
#     "Add Second": lambda x: [set_two.add(num) for num in x],
#     "Remove First": lambda x: [set_one.discard(num) for num in x],
#     "Remove Second": lambda x: [set_two.discard(num) for num in x],
#     "Check Subset": lambda x: print(set_one.issubset(set_two) or set_two.issubset(set_one)),
# }
#
# for _ in range(n):
#     first, second, *data = input().split()
#     command = first + " " + second
#     func_mapper[command]([int(x) for x in data])
#
# print(", ".join(map(str, sorted(set_one))))
# print(", ".join(map(str, sorted(set_two))))

#### Milkshakes ######
#
# from collections import deque
#
# chocolates = deque([int(x) for x in input().split(", ")])
# milk = deque([int(x) for x in input().split(", ")])
# milkshakes = 0
#
# while chocolates and milk:
#     choco = chocolates.pop()
#     cup = milk.popleft()
#
#     if choco <= 0 and cup <= 0:
#         continue
#     if choco <= 0:
#         milk.appendleft(cup)
#         continue
#     if cup <= 0:
#         chocolates.append(choco)
#         continue
#
#     if choco == cup:
#         milkshakes += 1
#         if milkshakes == 5:
#             break
#         continue
#     choco -= 5
#     milk.append(cup)
#     chocolates.append(choco)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# if chocolates:
#     print(f"Chocolate: {', '.join(map(str, chocolates))}")
# else:
#     print("Chocolate: empty")
# if milk:
#     print(f"Milk: {', '.join(map(str, milk))}")
# else:
#     print("Milk: empty")

##### Expression Evaluator
# from functools import reduce
# from collections import deque
#
# operators = ["/", "+", "-", "*"]
# line = deque(int(x) if x.lstrip('-').isdigit() else x for x in input().split())
#
# while len(line) > 1:
#     temp = []
#     operator = ""
#     while True:
#         num = line.popleft()
#         if num in operators:
#             operator = num
#             break
#         temp.append(num)
#     if operator == "/":
#         result = reduce(lambda a, b: a // b, temp)
#     if operator == "*":
#         result = reduce(lambda a, b: a * b, temp)
#     if operator == "-":
#         result = reduce(lambda a, b: a - b, temp)
#     if operator == "+":
#         result = reduce(lambda a, b: a + b, temp)
#     line.appendleft(result)
# print(line[0])

#### Expression Evaluator Mapper
#
# from collections import deque
# from functools import reduce
#
# operators = {
#     "/": lambda x: reduce(lambda a, b: a // b, x),
#     "+": lambda x: reduce(lambda a, b: a + b, x),
#     "-": lambda x: reduce(lambda a, b: a - b, x),
#     "*": lambda x: reduce(lambda a, b: a * b, x),
# }
#
# line = deque(int(x) if x.lstrip('-').isdigit() else x for x in input().split())
#
# while len(line) > 1:
#     temp = []
#     operator = None
#     while True:
#         num = line.popleft()
#         if not isinstance(num, int):
#             operator = num
#             break
#         temp.append(num)
#     result = operators[operator](temp)
#     line.appendleft(result)
#
# print(line[0])


##### Honey
# from collections import deque
#
# func_mapper = {
#     "/": lambda x, a: abs(x / a) if a > 0 else 0,
#     "+": lambda x, a: abs(x + a),
#     "*": lambda x, a: abs(x * a),
#     "-": lambda x, a: abs(x - a),
# }
#
# honey = 0
# bees = deque([int(x) for x in input().split()])
# nectar = [int(x) for x in input().split()]
# symbols = deque([x for x in input().split()])
#
# while bees and nectar:
#     bee = bees.popleft()
#     gathered = nectar.pop()
#     if gathered < bee:
#         bees.appendleft(bee)
#         continue
#     operator = symbols.popleft()
#     result = func_mapper[operator](bee, gathered)
#
#     honey += result
#
# print(f"Total honey made: {honey}")
# if bees:
#     print(f"Bees left: {', '.join(map(str, bees))}")
# if nectar:
#     print(f"Nectar left: {', '.join(map(str, nectar))}")

#### Santa's Present Factory

from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presents = {
    "Doll": {
        'built': False,
        'quantity': 0,
    },
    "Wooden train": {
        'built': False,
        'quantity': 0,
    },
    "Teddy bear": {
        'built': False,
        'quantity': 0,
    },
    "Bicycle": {
        'built': False,
        'quantity': 0,
    },
}

while materials and magic:
    box = materials.pop()
    spell = magic.popleft()

    if box == 0 and spell == 0:
        continue
    if box == 0:
        magic.appendleft(spell)
        continue
    if spell == 0:
        materials.append(box)
        continue

    value = box * spell

    if value < 0:
        amount = box + spell
        materials.append(amount)
        continue

    if value == 150:
        presents["Doll"]['built'] = True
        presents["Doll"]['quantity'] += 1
    elif value == 250:
        presents["Wooden train"]['built'] = True
        presents["Wooden train"]['quantity'] += 1
    elif value == 300:
        presents["Teddy bear"]['built'] = True
        presents["Teddy bear"]['quantity'] += 1
    elif value == 400:
        presents["Bicycle"]['built'] = True
        presents["Bicycle"]['quantity'] += 1
    else:
        box += 15
        materials.append(box)

if (presents["Doll"]['built'] and presents["Wooden train"]['built']) or \
        (presents["Bicycle"]['built'] and presents["Teddy bear"]['built']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

sorted_presents = dict(sorted(presents.items()))

for key, values in sorted_presents.items():
    if values['quantity'] > 0:
        print(f"{key}: {values['quantity']}")
