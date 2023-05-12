##### Count Same Values ######

# Solution with Counter
# from collections import Counter
#
# line = (float(x) for x in input().split())
#
# numbers = Counter(line)
#
# for key, value in numbers.items():
#     print(f"{key:.1f} - {value} times")

#### Students' Grades #####

# n = int(input())
# students = {}
#
# for _ in range(n):
#     name, grade = input().split()
#     if name in students:
#         students[name].append(float(grade))
#     else:
#         students[name] = [float(grade), ]
#
# for student, grades in students.items():
#     print(f"{student} ->", end=" ")
#     for grade in grades:
#         print(f"{grade:.2f}", end=" ")
#     print(f"(avg: {sum(grades) / len(grades):.2f})")

##### Record Unique Names #######
#
# names = set()
# n = int(input())
#
# for _ in range(n):
#     names.add(input())
#
# print("\n".join(names))

###### Parking Lot ########
# plates = set()
#
# mapper = {
#     "IN": lambda x: plates.add(x),
#     "OUT": lambda x: plates.remove(x),
# }
#
# n = int(input())
#
# for _ in range(n):
#     command, plate = input().split(", ")
#     mapper[command](plate)
#
# if plates:
#     print("\n".join(plates))
# else:
#     print("Parking Lot is Empty")

##### SoftUni Party #######
# guests = set()
# actual_guests = set()
# guests_number = int(input())
#
# for _ in range(guests_number):
#     guests.add(input())
# while True:
#     came = input()
#     if came == "END":
#         break
#     actual_guests.add(came)
#
# absent = sorted(guests.difference(actual_guests))
# print(len(absent))
# print("\n".join(absent))
