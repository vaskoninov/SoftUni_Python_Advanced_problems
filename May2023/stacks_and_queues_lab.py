##### Reverse Strings ######

# def reverse_string(text):
#     stack = [i for i in text]
#     reversed_string = []
#     while stack:
#         reversed_string.append(stack.pop())
#     return "".join(reversed_string)
#
#
# line = input()
#
# print(reverse_string(line))

########### Matching Parentheses ##########


# def find_indexes(expression):
#     parentheses_stack = []
#     pairs = []
#     for i, v in enumerate(expression):
#         if v == "(":
#             parentheses_stack.append(i)
#         if v == ")":
#             pairs.append((parentheses_stack.pop(), i))
#     return pairs
#
#
# def print_expressions(sequence, expression):
#     small_expressions = []
#     for pair in sequence:
#         small_expressions.append(expression[pair[0]:pair[1] + 1])
#     return "\n".join(small_expressions)
#
#
# line = input()
# indexes = find_indexes(line)
# print(print_expressions(indexes, line))

######## Supermarket ##########

# from collections import deque
#
# line = deque()
#
# while True:
#     name = input()
#     if name == "End":
#         print(f"{len(line)} people remaining.")
#         break
#     if name == "Paid":
#         while len(line) > 0:
#             print(line.popleft())
#         continue
#     line.append(name)

######## Water Dispenser ###########
# from collections import deque
#
# water = int(input())
#
# people = deque()
#
# while True:
#     line = input()
#     if line == "Start":
#         break
#     people.append(line)
#
# while True:
#     line = input()
#     if line == "End":
#         print(f"{water} liters left")
#         break
#     instructions = line.split()
#     if instructions[0] == "refill":
#         water += int(instructions[1])
#     else:
#         thirst = int(instructions[0])
#         if thirst <= water:
#             water -= thirst
#             print(f"{people.popleft()} got water")
#         else:
#             print(f"{people.popleft()} must wait")

##### Hot Potato ########
#
# from collections import deque
#
#
# def hot_potato(sequence, n):
#     counter = 1
#     while counter != n:
#         name = sequence.popleft()
#         counter += 1
#         sequence.append(name)
#     return f"Removed {sequence.popleft()}"
#
#
# kids = deque(input().split())
# rotation = int(input())
#
# while len(kids) > 1:
#     print(hot_potato(kids, rotation))
# print(f"Last is {kids[0]}")

#### Hot Potato 2 ######

from collections import deque

dd = deque(input().split())
n = int(input())

while len(dd) > 1:
    dd.rotate(-n + 1)
    print(f"Removed {dd.popleft()}")

print(f"Last is {dd[0]}")
