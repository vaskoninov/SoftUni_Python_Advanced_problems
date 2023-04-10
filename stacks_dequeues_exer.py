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
