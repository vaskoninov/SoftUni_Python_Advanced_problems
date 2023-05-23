# ######## Apocalypse Preparation

# from collections import deque

# items = {
#     "Patch": 0,
#     "Bandage": 0,
#     "MedKit": 0,
# }


# textiles = deque([int(x) for x in input().split()])
# medicaments = deque([int(x) for x in input().split()])

# while textiles and medicaments:
#     textile = textiles.popleft()
#     medicament = medicaments.pop()

#     resource = textile + medicament

#     if resource == 30:
#         items["Patch"] += 1
#     elif resource == 40:
#         items["Bandage"] += 1
#     elif resource >= 100:
#         items["MedKit"] += 1
    
#         if resource > 100:
#             rest = resource - 100
#             medicaments[-1] += rest

#     else:
#         medicaments.append(medicament + 10)

# if not textiles and not medicaments:
#     print("Textiles and medicaments are both empty.")
# elif not textiles:
#     print("Textiles are empty.")
# elif not medicaments:
#     print("Medicaments are empty.")

# for item, numbers in sorted(items.items(), key=lambda x: (-x[1], x[0])):
#     if numbers > 0:
#         print(f"{item} - {numbers}")
# if medicaments:
#     print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
# if textiles:
#     print(f"Textiles left: {', '.join(map(str, textiles))}")

######## Blind Man's Buff

# def is_valid(n, m):
#     return n in range(rows) and m in range(cols)


# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
# blind = ()
# players = 0
# moves = 0
# playground = []

# rows, cols = [int(x) for x in input().split()]

# for i in range(rows):
#     line = input().split()
#     playground.append(line)
#     if "B" in line:
#         blind = (i, line.index("B"))

# direction = input()
# all_touched = False

# while direction != "Finish":

#     new_position = (
#         blind[0] + movements[direction][0], \
#             blind[1] + movements[direction][1]
#         )
#     if is_valid(new_position[0], new_position[1]) \
#     and playground[new_position[0]][new_position[1]] != "O":
    
#         playground[blind[0]][blind[1]] = "-"
#         moves += 1
#         if playground[new_position[0]][new_position[1]] == "P":
#             players += 1
#             if players == 3:
#                 all_touched = True
#         blind = (new_position[0], new_position[1])
#         playground[blind[0]][blind[1]] = "B"
#     if all_touched:
#         break
    
#     direction = input()
        

# print("Game over!")
# print(f"Touched opponents: {players} Moves made: {moves}")

##### Grocery List

def shop_from_grocery_list(money, grocery_list, *args):
    budget = money
    purchased = []
    products = [args[0] for args in args]

    for product, price in args:
        if product not in grocery_list or product in purchased:
            continue
        if budget < float(price):
            break
        budget -= float(price)
        purchased.append(product)
        
    
    not_bought = []
    for item in grocery_list:
        if item not in purchased:
            not_bought.append(item)

    if not not_bought:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(not_bought)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(100, ["tomato", "cola", "chips", "meat"], \
    ("cola", 5.8), ("tomato", 10.0), ("meat", 22), ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
