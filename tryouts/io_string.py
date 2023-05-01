# import sys
# from io import StringIO
#
# test = "hello world"
#
# sys.stdin = StringIO(test)
#
# print(test)
########
# for i in range(-1, 2, 1):
#     print(i)
##############
ll = [1, 2, 3, 4]

print(*ll)


def f(*args):
    return sum(args)


print(f(ll))
