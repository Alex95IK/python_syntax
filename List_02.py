from timeit import timeit

#
# n = list(range(1, 11))
#
# print(n)
#
# x = ''.join(i for i in range(1, 11))
#
# print(x)


def one():
    return ''.join(map(str, range(100)))


def two():
    return ''.join(str(i) for i in range(100))


print(timeit(one))

print(timeit(two))
