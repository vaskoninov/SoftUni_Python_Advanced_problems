#### Multiplication Function

# def multiply(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result
#
#
# print(multiply(1, 4, 5))

##### Person Info
#
# def get_info(**kwargs):
#     return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


##### Cheese Showcase
#
# def sorting_cheeses(**kwargs):
#     final_list = []
#     cheese = {k: sorted(v, reverse=True) for k, v in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))}
#     for product, value in cheese.items():
#         final_list.append(product)
#         for v in value:
#             final_list.append(str(v))
#
#     return "\n".join(final_list)
#
#
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )

##### Rectangle

# def rectangle(a, b):
#     def area():
#         return a * b
#
#     def perimeter():
#         return 2 * a + 2 * b
#
#     if not isinstance(a, int) or not isinstance(b, int):
#         return "Enter valid values!"
#
#     return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
#
#
# print(rectangle(2, 10))
# print(rectangle("a", 10))

##### Operate

# def operate(*args):
#     def add(*args):
#         return sum(args)
#
#     def subtract(*args):
#         result = args[0]
#         for i in args[1:]:
#             result -= i
#         return result
#
#     def multiply(*args):
#         result = 1
#         for i in args:
#             result *= i
#         return result
#
#     def divide(*args):
#         result = args[0]
#         for i in args[1:]:
#             result /= i
#         return result
#
#     operator, *nums = args
#
#     operations = {
#         "+": add,
#         "-": subtract,
#         "*": multiply,
#         "/": divide,
#     }
#
#     return operations[operator](*nums)
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

##### Recursive Power

def recursive_power(number, power):
    if power == 1:
        return number

    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
