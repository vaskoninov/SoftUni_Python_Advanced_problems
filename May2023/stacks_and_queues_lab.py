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

from collections import deque

line = deque()

while True:
    name = input()
    if name == "End":
        print(f"{len(line)} people remaining.")
        break
    if name == "Paid":
        while len(line) > 0:
            print(line.popleft())
        continue
    line.append(name)
