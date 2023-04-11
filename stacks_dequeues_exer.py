# stack = input().split()
#
# while stack:
#     print(stack.pop(), end=" ")

#################

# stack = []
# n = int(input())
#
# for i in range(n):
#     query = input()
#     if query.startswith("1"):
#         commands = query.split()
#         stack.append(int(commands[1]))
#     if stack:
#         if query == "2":
#             stack.pop()
#         if query == "3":
#             print(max(stack))
#         if query == "4":
#             print(min(stack))
#
# print(", ".join(map(str, reversed(stack))))

##################
# from collections import deque
#
# food = int(input())
# orders = deque([int(x) for x in input().split()])
#
# print(max(orders))
#
# while orders:
#     order = orders[0]
#     if order <= food:
#         food -= order
#         orders.popleft()
#     else:
#         break
#
# if orders:
#     print(f"Orders left: {' '.join(map(str, orders))}")
# else:
#     print("Orders complete")

#################

# stack = [int(x) for x in input().split()]
#
# rack_capacity = int(input())
# curr_rack = 0
# racks = 1
#
# while stack:
#     clothing = stack.pop()
#     if curr_rack + clothing > rack_capacity:
#         curr_rack = clothing
#         racks += 1
#     else:
#         curr_rack += clothing
#
# print(racks)

#################
# from collections import deque
#
# pump_deque = deque()
# pumps = int(input())
#
# for i in range(pumps):
#     fuel, distance = input().split()
#     pump_deque.append((int(fuel), int(distance)))
#
# for i in range(pumps):
#     tank = 0
#     stops = 0
#     for pump in pump_deque:
#         fuel, distance = pump
#
#         tank += fuel
#
#         if tank < distance:
#             break
#
#         stops += 1
#         tank -= distance
#
#     if stops == len(pump_deque):
#         print(i)
#         break
#
#     pump_deque.rotate(-1)
####################
#
# line = input()
# stack = []
# balanced = False
#
# for i in line:
#     if i == '(' or i == "{" or i == "[":
#         stack.append(i)
#     else:
#         if stack:
#             t = stack.pop()
#             if i == ")" and t == "(":
#                 continue
#             elif i == "}" and t == "{":
#                 continue
#             elif i == "]" and t == "[":
#                 continue
#             else:
#                 break
#         else:
#             break
# else:
#     balanced = True
#
# if balanced:
#     print("YES")
# else:
#     print("NO")

######################
# from collections import deque
#
# info_robots = input().split(";")
# robots = {}
# for info in info_robots:
#     info = info.split("-")
#     name = info[0]
#     time = int(info[1])
#     robots[name] = {}
#     robots[name]['time'] = time
#     robots[name]['is_working'] = False
#     robots[name]['counter'] = 0
#
# times = [int(x) for x in input().split(":")]
#
# products = deque()
#
# while True:
#     product = input()
#     if product == "End":
#         break
#     products.append(product)
#
# while products:
#     for key, values in robots.items():
#         if values['is_working']:
#             values['counter'] += 1
#     times[2] += 1
#     if times[2] == 60:
#         times[2] = 0
#         times[1] += 1
#         if times[1] == 60:
#             times[1] = 0
#             times[0] += 1
#             if times[0] == 24:
#                 times[0] = 0
#
#     for key, values in robots.items():
#         if values['counter'] % values['time'] == 0:
#             values["is_working"] = False
#
#     to_work = products.popleft()
#
#     for robot, values in robots.items():
#         if not values['is_working']:
#             values['is_working'] = True
#             name = robot
#             print(f"{name} - {to_work} [{times[0]:02}:{times[1]:02}:{times[2]:02}]")
#             break
#     else:
#         products.append(to_work)

####################
# from collections import deque
#
# green_duration = int(input())
# free_window = int(input())
#
# cars = deque()
# counter = 0
# passed = []
# safety = True
#
# while safety:
#     commands = input()
#     if commands == "END":
#         break
#     if commands == "green":
#         safety_time = green_duration
#         while safety_time > 0:
#             if cars:
#                 passing = cars.popleft()
#                 if len(passing) <= safety_time:
#                     counter += 1
#                     passed.append(passing)
#                     safety_time -= len(passing)
#                 else:
#                     rest = abs(safety_time - len(passing))
#                     if rest <= free_window:
#                         counter += 1
#                         passed.append(passing)
#                         break
#                     else:
#                         hit = abs(free_window - rest)
#                         char = passing[-hit]
#                         print("A crash happened!")
#                         print(f"{passing} was hit at {char}.")
#                         safety = False
#                         break
#             else:
#                 break
#     else:
#         cars.append(commands)
#
# if safety:
#     print("Everyone is safe.")
#     print(f"{counter} total cars passed the crossroads.")

####################
