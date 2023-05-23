players = 0
command = input()

while players < 3 and command != "e":
    players += 1
    command = input()    
print(players)

# args = [("p", 1), ("s", 2)]
# products = [args[0] for args in args]

# print(products)