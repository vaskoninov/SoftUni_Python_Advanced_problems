##### Energy Drinks ######

# from collections import deque
#
# stamat_caffeine = 0
#
# caffeine = deque([int(x) for x in input().split(", ")])
# drinks = deque([int(x) for x in input().split(", ")])
#
# while caffeine and drinks:
#     caf = caffeine.pop()
#     drink = drinks.popleft()
#
#     if caf * drink + stamat_caffeine <= 300:
#         stamat_caffeine += caf * drink
#     elif caf * drink + stamat_caffeine > 300:
#         drinks.append(drink)
#         stamat_caffeine -= 30
#         if stamat_caffeine < 0:
#             stamat_caffeine = 0
#
# if drinks:
#     print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
# else:
#     print("At least Stamat wasn't exceeding the maximum caffeine.")
# print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")

###### Rally Racing ######
#
# movements = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# size = int(input())
# racing_number = input()
# matrix = []
# car = (0, 0)
# km = 0
# tunnels = []
# final = ()
#
# for i in range(size):
#     matrix.append(input().split())
#     if "T" in matrix[i]:
#         tunnels.append((i, matrix[i].index("T")))
#     if "F" in matrix[i]:
#         final = (i, matrix[i].index("F"))
#
# while True:
#     command = input()
#     if command == "End":
#         matrix[car[0]][car[1]] = "C"
#         print(f"Racing car {racing_number} DNF.")
#         break
#     matrix[car[0]][car[1]] = "."
#     car = (car[0] + movements[command][0], car[1] + movements[command][1])
#     if matrix[car[0]][car[1]] == ".":
#         matrix[car[0]][car[1]] = "C"
#         km += 10
#     if matrix[car[0]][car[1]] == "T":
#         matrix[car[0]][car[1]] = "."
#         tunnels.remove((car[0], car[1]))
#         car = (tunnels[0][0], tunnels[0][1])
#         matrix[car[0]][car[1]] = "."
#         km += 30
#     if matrix[car[0]][car[1]] == "F":
#         matrix[car[0]][car[1]] = "C"
#         km += 10
#         print(f"Racing car {racing_number} finished the stage!")
#         break
# print(f"Distance covered {km} km.")
# for row in matrix:
#     print("".join(row))


##### Hourly Forecast

def forecast(*args):
    locations = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }

    result = []

    for loc, weather in args:
        for key in locations:
            if weather == key:
                locations[key].append(loc)
                break
    for key, value in locations.items():
        locations[key] = sorted(value)

    for key, value in locations.items():
        for loc in value:
            result.append(f"{loc} - {key}")

    return "\n".join(result)


# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
