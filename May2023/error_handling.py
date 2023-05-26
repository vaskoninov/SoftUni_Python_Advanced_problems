#### So Many Exceptions
# numbers_list = [int(x) for x in input().split(", ")]
# result = 1
#
# for number in numbers_list:
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
# print(f"{result:.1f}")

##### Repeat Text
#
# text = input()
# while True:
#     try:
#         n = int(input())
#         break
#     except ValueError:
#         print("Variable times must be an integer")
# print(text * n)

######
class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    n = int(input())
    if n < 0:
        raise ValueCannotBeNegative("the num is negative")
