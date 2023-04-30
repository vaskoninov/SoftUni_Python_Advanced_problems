# Packing and Unpacking arguments
# *args and **kwargs

# ll = [1, 2, 3, 4]

# x, y, *z = ll
# print(x)
# print(y)

# k, *l, r = ll
# print(k)
# print(r)
#
# k, *_, r = ll
# print(k)
# print(r)

## Packing
# *args
# def f(*args):
#     """
#     the function can take zero or more arguments
#     :param args:
#     :return:
#     """
#     print(args)
#
#
# f(1)

# **kwargs
# allow to pass keyworded variable length of arguments to a function

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{value}, {key}")

# def f(**kwargs):
#     if "age" not in kwargs:
#         kwargs['age'] = None
#     return kwargs
#
#
# print(f(name="Peter", family=19))

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# func(1, 2, 3)
# func(1, 2, 3, name="Peter")

# Formal Args, *args, **kwargs
# formal args are AKA positional args
# always positional args take their values

# def func_2(x, *args, **kwargs):
#     print(f"x={x}, args={args}, kwargs={kwargs}")
#
#
# func_2(1, 2, key="xyz")

# ll1 = [1, 2, 3, 4]
#
# k, l, *r = ll1
#
# ll2 = [-1, *ll1, -2]
# print(ll2)

# dd1 = {
#     'x': 1,
#     'y': 2,
# }
#
# dd2 = {
#     'z': 3,
#     **dd1
# }
#
# print(dd2)
#
# def f(*args, **kwargs):
#     print(f"args = {args}, kwargs = {kwargs}")
#
#
# numbers = [1, 2, 3, 4, 5]
#
# grades = {
#     'Peter': 3,
#     'Maria': 4,
#     'Stoil': 5,
# }
#
# f(*numbers)
# f(**grades)
# f(*numbers, **grades)


# def tell_score(Maria, **kwargs):
#     print(f"Peter has {Maria}")
#
#
# tell_score(**grades)

###############
# Multiply function

# def multiply(*args):
#     result = 1
#     for i in args:
#         result *= i
#     return result

# GetInfo Function

# def get_info(**kwargs):
#     return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

# def sorting_cheeses(**kwargs):
#     for key in kwargs:
#         kwargs[key] = sorted(kwargs[key], reverse=True)
#
#     sorted_cheese = dict(sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])))
#
#     result = []
#     for cheese, value in sorted_cheese.items():
#         result.append(cheese)
#         for v in value:
#             result.append(str(v))
#
#     return "\n".join(result)
# print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125], ))

#############


# def rectangle(a, b):
#     if not isinstance(a, int) or not isinstance(b, int):
#         return "Enter valid values!"
#
#     def area(a, b):
#         return a * b
#
#     def perimeter(a, b):
#         return 2 * a + 2 * b
#
#     return f"Rectangle area: {area(a, b)}\nRectangle perimeter: {perimeter(a, b)}"
#
#
# print(rectangle(2, 10))
# print(rectangle("a", 10))

###############

def operate(operator, *args):
    def addition(*args):
        result = 0
        for i in args:
            result += i
        return result

    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result

    def division(*args):
        result = args[0]
        for i in args[1:]:
            result /= i
        return result

    def subtractions(*args):
        result = args[0]
        for i in args[1:]:
            result -= i
        return result

    if operator == "+":
        return addition(args)
    elif operator == "-":
        return subtractions(args)
    elif operator == "*":
        return multiply(args)
    elif operator == "/":
        return division(args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
