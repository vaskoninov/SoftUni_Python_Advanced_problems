# name = "Barbara"
# c = Counter(name.lower())
# print(c)
# from collections import deque
#
# dd = deque(["George", "Peter", "Michael", "William", "Thomas"])
# n = 10
#
# while len(dd) > 1:
#     dd.rotate(-n + 1)
#     print(f"Removed {dd.popleft()}")
#
# print(f"Last is {dd[0]}")
################
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

#############
