# n = int(input())
#
# names = set()
#
# for _ in range(n):
#     names.add(input())
# print("\n".join(names))

################

# set_one = set()
#
# set_two = set()
#
# num_one, num_two = [int(x) for x in input().split()]
#
# for _ in range(num_one):
#     set_one.add(int(input()))
# for _ in range(num_two):
#     set_two.add(int(input()))
#
# common = set_one.intersection(set_two)
# print("\n".join(map(str, common)))

#################
#
# elements = set()
# n = int(input())
#
# for _ in range(n):
#     nums = [x for x in input().split()]
#     for num in nums:
#         elements.add(num)
#
# print("\n".join(elements))

###################
# from collections import Counter
#
# line = input()
# c = Counter(line)
#
# s = sorted(c.items())
#
# for pair in s:
#     print(f"{pair[0]}: {pair[1]} time/s")

##################

# n = int(input())
#
# l_length = 0
# longest = []
#
# for _ in range(n):
#     line = [x for x in input().split("-")]
#     temp1 = [int(x) for x in line[0].split(",")]
#     temp2 = [int(x) for x in line[1].split(",")]
#     range1 = set(range(temp1[0], temp1[1] + 1))
#     range2 = set(range(temp2[0], temp2[1] + 1))
#
#     intersection = range1.intersection(range2)
#     length = len(intersection)
#     if length > l_length:
#         l_length = length
#         longest = intersection
#
# print(f"Longest intersection is [{', '.join(map(str, list(longest)))}] with length {l_length}")

##################

n = int(input())
odd = set()
even = set()

for i in range(1, n + 1):
    name = [ord(x) for x in input()]
    value = sum(name)
    final = value // i
    if final % 2 == 0:
        even.add(final)
    else:
        odd.add(final)

value_odd = sum(odd)
value_even = sum(even)

if value_odd == value_even:
    p = odd.union(even)
elif value_odd > value_even:
    p = odd.difference(even)
else:
    p = odd.symmetric_difference(even)

print(", ".join(map(str, p)))
