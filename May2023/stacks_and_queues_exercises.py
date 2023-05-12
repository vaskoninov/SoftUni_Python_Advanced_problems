#### Reverse numbers ########

# def reverse_numbers(sequence):
#     reverse_seq = []
#     while sequence:
#         reverse_seq.append(sequence.pop())
#     return " ".join(reverse_seq)


# numbers = input().split()
# print(reverse_numbers(numbers))


##### Stacked queries ########

# from collections import deque
#
# numbers = deque()
#
# for _ in range(int(input())):
#     data = [int(x) for x in input().split()]
#     if data[0] != 1:
#         if numbers:
#             if data[0] == 2:
#                 numbers.pop()
#             if data[0] == 3:
#                 print(max(numbers))
#             if data[0] == 4:
#                 print(min(numbers))
#     else:
#         numbers.append(data[1])
# else:
#     print(", ".join(map(str, reversed(numbers))))

# from collections import deque
#
# numbers = deque()
#
# mapper = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     data = [int(x) for x in input().split()]
#     mapper[data[0]](data)
#
# numbers.reverse()
# print(*numbers, sep=", ")


######## Fast Food ########

# from collections import deque

# food = int(input())

# orders = deque([int(x) for x in input().split()])

# print(max(orders))

# while food > 0 and orders:
#     order = orders.popleft()
#     if order <= food:
#         food -= order
#     else:
#         orders.appendleft(order)
#         break
# else:
#     print("Orders complete")

# if orders:
#     print(f'Orders left: {" ".join(map(str, orders))}')

###### Fashion Boutique #########

# clothings = [int(x) for x in input().split()]

# rack_capacity = int(input())
# current = 0
# racks = 1

# while clothings:

#     clothes = clothings.pop()
#     if clothes + current > rack_capacity:
#         racks += 1
#         current = clothes
#     else:
#         current += clothes

# print(racks)

#### Truck Tour ####

# from collections import deque


# pumps = int(input())
# data = deque([])


# for i in range(pumps):
#     data.append([int(x) for x in input().split()])

# for i in range(pumps):

#     tank = 0
#     stops = 0   

#     for pump in data:
#         current = pump
#         tank += current[0]

#         if tank < current[1]:
#             break

#         tank -= current[1]
#         stops += 1
#     if stops == pumps:
#         print(i)
#         break
#     data.rotate(-1)

#### Balanced Parentheses ######
# stack = []
# parentheses = input()

# for i, v in enumerate(parentheses):
#     if v == "(" or v == "{" or v == "[":
#         stack.append(v)
#     else:
#         if stack:
#             p = stack.pop()
#             if p == "(" and v == ")":
#                 continue
#             elif p == "{" and v == "}":
#                 continue
#             elif p == "[" and v == "]":
#                 continue
#             else:
#                 print("NO")
#                 break
#         else:
#             print("NO")
#             break
# else:
#     print("YES")

####### Robotics #########

# from collections import deque


# workers = input().split(";")

# robots = {}

# for worker in workers:
#     name, proc = worker.split("-")
#     robots[name] = {}
#     robots[name]["proc_time"] = int(proc)
#     robots[name]["is_working"] = False
#     robots[name]["time"] = 0


# hours, minutes, seconds = [int(x) for x in input().split(":")]

# products = deque()
# while True:
#     product = input()
#     if product == "End":
#         break
#     products.append(product)

# while products:

#     for robot, value in robots.items():
#         if value["is_working"]:
#             value["time"] += 1

#     seconds += 1
#     if seconds == 60:
#         seconds = 0
#         minutes += 1
#         if minutes == 60:
#             minutes = 0
#             hours += 1
#             if hours == 24:
#                 hours = 0


#     for robot, informations in robots.items():
#         if informations["time"] % informations["proc_time"] == 0:
#             informations["is_working"] = False

#     product = products.popleft()

#     for robot, informations in robots.items():
#         if not informations["is_working"]:
#             informations["is_working"] = True
#             print(f"{robot} - {product} [{hours:02}:{minutes:02}:{seconds:02}]")
#             break
#     else:
#         products.append(product)

####### Crossroads ##########

# from collections import deque


# green = int(input())

# free_window = int(input())

# cars = deque()
# passed = 0
# crashless = True


# while crashless:
#     line = input()
#     if line == "END":
#         break
#     if line == "green":
#         green_light = green
#         while green_light and cars:
#             car = cars.popleft()
#             if len(car) <= green_light:
#                 green_light -= len(car)
#                 passed += 1
#             else:
#                 rest = len(car) - green_light
#                 if rest <= free_window:
#                     passed += 1
#                     break
#                 else:
#                     hit = abs(rest - free_window)
#                     char = car[-hit]
#                     crashless = False
#                     print("A crash happened!")
#                     print(f"{car} was hit at {char}.")
#                     break
#     else:
#         cars.append(line)

# if crashless:
#     print("Everyone is safe.")
#     print(f"{passed} total cars passed the crossroads.")

####### Key Revolver ##########

# from collections import deque


# price = int(input())
# barrel = int(input())
# bullets = [int(x) for x in input().split()]
# locks = deque([int(x) for x in input().split()])
# value = int(input())
# used_bullets = 0

# while bullets and locks:
#     bullet = bullets.pop()
#     lock = locks.popleft()
#     if lock >= bullet:
#         print("Bang!")
#     else:
#         locks.appendleft(lock)
#         print("Ping!")
#     used_bullets += 1
#     if used_bullets % barrel == 0 and bullets:
#         print("Reloading!")

# if locks:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# else:
#     print(f"{len(bullets)} bullets left. Earned ${value - (price * used_bullets)}")

###### Cups and Bottles #####

from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
water = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        cup -= bottle
        if cup <= 0:
            water += abs(cup)

if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
    print(f"Wasted litters of water: {water}")
else:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")
    print(f"Wasted litters of water: {water}")
