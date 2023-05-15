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

from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while chocolates and milk:
    choco = chocolates.pop()
    cup = milk.popleft()

    if choco <= 0 and cup <= 0:
        continue
    if choco <= 0:
        milk.appendleft(cup)
        continue
    if cup <= 0:
        chocolates.append(choco)
        continue

    if choco == cup:
        milkshakes += 1
        if milkshakes == 5:
            break
        continue
    choco -= 5
    milk.append(cup)
    chocolates.append(choco)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
