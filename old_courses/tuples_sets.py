##### Tuples and Sets

# Tuples - read-only collections
# from collections import Counter
#
# line = (float(x) for x in input().split())
#
# occurences = Counter(line)
#
# for key, value in occurences.items():
#     print(f"{key} - {value} times")

#################

# n = int(input())
# students = {}
#
# for _ in range(n):
#     name, grade = tuple(input().split())
#     if name not in students:
#         students[name] = []
#     students[name].append(float(grade))
#
# for key, value in students.items():
#     aver = sum(value) / len(value)
#     print(f"{key} ->", end=" ")
#     for i in value:
#         print(f"{i:.2f}", end=" ")
#     print(f"(avg: {aver:.2f})")

####################
# names = set()
# n = int(input())
# for _ in range(n):
#     names.add(input())
# print("\n".join(names))

#####################

# parking = set()
# n = int(input())
#
# for _ in range(n):
#     command, plate = input().split(", ")
#     if command == "IN":
#         parking.add(plate)
#     if command == "OUT":
#         parking.remove(plate)
# if parking:
#     print("\n".join(parking))
# else:
#     print("Parking Lot is Empty")

###############

# guest_list = set()
# actual_guests = set()
# n = int(input())
#
# for _ in range(n):
#     guest_list.add(input())
#
# while True:
#     guest = input()
#     if guest == "END":
#         break
#     actual_guests.add(guest)
#
# absent = sorted(guest_list - actual_guests)
# print(len(absent))
# print("\n".join(absent))

###############
iterations = set()
nums = [int(x) for x in input().split()]
target = int(input())
counter = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        counter += 1
        if nums[i] + nums[j] == target:
            print(f"{nums[i]} + {nums[j]} = {target}")
            iterations.add((nums[i], nums[j]))
print(f"Iterations done: {counter}")
iterations_list = [x for x in iterations]
for i in iterations_list:
    print(i)
