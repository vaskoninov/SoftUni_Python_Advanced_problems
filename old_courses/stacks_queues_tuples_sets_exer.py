# from collections import deque
#
# set_one = set([int(x) for x in input().split()])
# set_two = set([int(x) for x in input().split()])
#
# n = int(input())
#
# for _ in range(n):
#     command = deque(input().split())
#     initial_command = command.popleft()
#     if initial_command == "Add":
#         set_name = command.popleft()
#         if set_name == "First":
#             while command:
#                 num = int(command.popleft())
#                 set_one.add(num)
#         else:
#             while command:
#                 num = int(command.popleft())
#                 set_two.add(num)
#     elif initial_command == "Remove":
#         set_name = command.popleft()
#         if set_name == "First":
#             while command:
#                 num = int(command.popleft())
#                 if num in set_one:
#                     set_one.remove(num)
#         else:
#             while command:
#                 num = int(command.popleft())
#                 if num in set_two:
#                     set_two.remove(num)
#     else:
#         print(set_one.issubset(set_two) or set_two.issubset(set_one))
# print(", ".join(map(str, sorted(set_one))))
# print(", ".join(map(str, sorted(set_two))))


# from collections import deque
# #####################
# from functools import reduce
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

#####################
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

#################

from collections import deque

honey = 0
bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])

while bees and nectar:
    result = 0
    bee = bees.popleft()
    gathered = nectar.pop()
    if gathered < bee:
        bees.appendleft(bee)
        continue
    operator = symbols.popleft()
    if operator == "/":
        if gathered > 0:
            result = abs(bee / gathered)
        else:
            result = 0
    if operator == "*":
        result = abs(bee * gathered)
    if operator == "+":
        result = abs(bee + gathered)
    if operator == "-":
        result = abs(bee - gathered)
    honey += result

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
