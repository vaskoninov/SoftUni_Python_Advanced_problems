### Unique Usernames
#
# n = int(input())
# names = set(input() for _ in range(n))
#
# print("\n".join(names))
#### Sets of Elements

# n, m = [int(x) for x in input().split()]
#
# first = set([int(input()) for _ in range(n)])
# second = set([int(input()) for _ in range(m)])
#
# third = first & second
# print("\n".join([str(x) for x in third]))

#### Periodic Table
# elements = set()
# n = int(input())
#
# for _ in range(n):
#     elements_input = input().split()
#     elements.update(elements_input)
#
# print("\n".join(elements))

###### Count Symbols

# from collections import Counter
#
# line = input()
# counter = Counter(line)
#
# for key, value in sorted(counter.items()):
#     print(f"{key}: {value} time/s")

####### Longest Intersection
# import sys
#
# n = int(input())
# longest = []
# llength = -sys.maxsize
#
# for _ in range(n):
#     line = input().split("-")
#     nums1 = [int(x) for x in line[0].split(",")]
#     nums2 = [int(x) for x in line[1].split(",")]
#     set1 = set(x for x in range(nums1[0], nums1[1] + 1))
#     set2 = set(x for x in range(nums2[0], nums2[1] + 1))
#
#     intersection = set1.intersection(set2)
#     length = len(intersection)
#     if length > llength:
#         llength = length
#         longest = intersection
#
# print(f'Longest intersection is [{", ".join(map(str, longest))}] with length \
# {llength}')

####### Battle of Names

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
