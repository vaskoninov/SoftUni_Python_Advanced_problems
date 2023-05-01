# def sum_positives(*args):
#     return sum(int(x) for x in args if x > 0)
#
#
# def sum_negatives(*args):
#     return sum(int(x) for x in args if x < 0)
#
#
# ll = [int(x) for x in input().split()]
#
# print(sum_negatives(*ll))
# print(sum_positives(*ll))
# if sum_positives(*ll) > abs(sum_negatives(*ll)):
#     print("The positives are stronger than the negatives")
# else:
#     print("The negatives are stronger than the positives")

##################
#
# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# dictionary = {'name': 'Peter', 'age': 25}
#
# print(kwargs_length(**dictionary))

###################
#
# def even_odd(*args):
#     command = args[-1]
#
#     if command == "even":
#         return [x for x in args[:-1] if x % 2 == 0]
#     else:
#         return [x for x in args[:-1] if x % 2 != 0]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

##################
#
# def even_odd_filter(**kwargs):
#     result = {}
#
#     for key in kwargs:
#         if key == "odd":
#             result[key] = [x for x in kwargs[key] if x % 2 != 0]
#         elif key == "even":
#             result[key] = [x for x in kwargs[key] if x % 2 == 0]
#
#     sorted_result = dict(sorted(result.items(), key=lambda x: -len(x[1])))
#
#     return sorted_result
#
#
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))

###################
#
# def concatenate(*args, **kwargs):
#     result = ''
#     for arg in args:
#         result += arg
#
#     for k in kwargs:
#         if k in result:
#             result = result.replace(k, kwargs[k])
#     return result
#
#
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

####################
#
#
# def func_executor(*args):
#     final_list = []
#
#     for arg in args:
#         func = arg[0]
#         result = func(*arg[1])
#         final_list.append(f"{arg[0].__name__} - {result}")
#
#     return "\n".join(final_list)
#
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
#
# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))

####################
#
#
# def grocery_store(**kwargs):
#     sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
#
#     result = []
#     for k, v in sorted_dict.items():
#         result.append(f"{k}: {v}")
#
#     return "\n".join(result)
#
#
# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
#
# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))

###########################
#
# def age_assignment(*args, **kwargs):
#     result = []
#     sorted_names = sorted(args)
#     for name in sorted_names:
#         for key in kwargs:
#             if name.startswith(key):
#                 result.append(f"{name} is {kwargs[key]} years old.")
#
#     return "\n".join(result)
#
#
# print(age_assignment("Peter", "George", G=26, P=19))

####################
#
# def palindrome(word, idx=0):
#     if idx == len(word) // 2:
#         return f"{word} is a palindrome"
#
#     if word[idx] == word[-idx - 1]:
#         return palindrome(word, idx + 1)
#     else:
#         return f"{word} is not a palindrome"
#
#
# print(palindrome("abcba", 0))

########################

# def fill_the_box(*args):
#     height, length, width, *other = args
#
#     box = height * length * width
#     end = other.index("Finish")
#     cubes = 0
#     for i, v in enumerate(other[:end]):
#         cubes += v
#
#         if cubes >= box:
#             other[i] = cubes - box
#             result = sum(other[:end])
#             return f"No more free space! You have {result} more cubes."
#         other[i] = 0
#     else:
#         result = box - cubes
#         return f"There is free space in the box. You could put {result} more cubes."
#
#
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

#####################

def math_operations(*args, **kwargs):
    results = {**kwargs}
    for i, v in enumerate(args):
        if i % 4 == 0:
            results["a"] = results["a"] + v
        if i % 4 == 1:
            results["s"] = results["s"] - v
        if i % 4 == 2:
            if v == 0:
                continue
            results["d"] = results["d"] / v
        if i % 4 == 3:
            results["m"] = results["m"] * v

    sorted_dictionary = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
    to_return = []

    for key, value in sorted_dictionary.items():
        to_return.append(f"{key}: {value:.1f}")

    return "\n".join(to_return)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
