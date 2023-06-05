def sum_nums(a, b):
    return a + b


def divide_nums(a, b):
    return a / b


def subtract_nums(a, b):
    return a - b


def multiply_nums(a, b):
    return a * b


def pow_nums(a, b):
    return a ** b


mapper = {
    "+": sum_nums,
    "-": subtract_nums,
    "*": multiply_nums,
    "/": divide_nums,
    "^": pow_nums,
}


def execute_string(expression):
    num1, sign, num2 = expression.split()
    num1 = float(num1)
    num2 = float(num2)

    return mapper[sign](num1, num2)


print(execute_string("2.5 * 2"))
