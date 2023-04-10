# Stacks - Last In First Out - LIFO


# Retrieving data with pop() method
# Actions: push, pop, peek, count/size
#
# Stack could be created with lists or doubly linked lists
#
# Operations in Stack should be with Big O (1)
#
# Main methods - append() and pop()

# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(stack)
#
# last_el = stack.pop()
# print(stack)
# print(last_el)
# print(stack[-1])
# print(len(stack))

####################
#
# stack = []
# line = input()
# reversed = []
#
# for i in line:
#     stack.append(i)
#
# while stack:
#     t = stack.pop()
#     reversed.append(t)
#
# print("".join(reversed))

####################
# stack = []
# indexes = []
# line = input()
#
# for i, v in enumerate(line):
#     if v == "(":
#         stack.append(i)
#     if v == ")":
#         initial = stack.pop()
#         end = i + 1
#         indexes.append((initial, end))
# for pair in indexes:
#     print(line[pair[0]:pair[1]])
##################

###############

# Queues - First In First Out
# - priority queues
# Actions - enqueue, dequeue Big O (1)

# Python uses collections.deque
# Methods: append(), popleft(), appendleft(), pop()
#
# from collections import deque
#
# q = deque([1, 2, 3])
#
# print(q)

################

# from collections import deque
#
# queue = deque()
#
# while True:
#     line = input()
#     if line == "End":
#         print(f"{len(queue)} people remaining.")
#         break
#     elif line == "Paid":
#         while queue:
#             name = queue.popleft()
#             print(name)
#     else:
#         queue.append(line)

################
# from collections import deque
#
# water = int(input())
# queue = deque()
#
# while True:
#     line = input()
#     if line == "Start":
#         break
#     else:
#         queue.append(line)
#
# while True:
#     commands = input()
#     if commands == "End":
#         print(f"{water} liters left")
#         break
#     if commands.startswith("refill"):
#         commands = commands.split()
#         water += int(commands[1])
#     else:
#         liters = int(commands)
#         name = queue.popleft()
#         if liters <= water:
#             print(f"{name} got water")
#             water -= liters
#         else:
#             print(f"{name} must wait")

#################
# from collections import deque
#
# kids = deque(input().split())
# turn = int(input())
#
# counter = 1
#
# while len(kids) > 1:
#     kid = kids.popleft()
#     if counter == turn:
#         print(f"Removed {kid}")
#         counter = 1
#     else:
#         counter += 1
#         kids.append(kid)
#
# winner = kids.popleft()
# print(f"Last is {winner}")

#############

## Queue rotate() method
