from timeit import timeit


def one():
    return list(map(lambda num: num * 2, range(1, 101)))


def two():
    return [x * 2 for x in range(1, 101)]


print(timeit(one))

print(timeit(two))


def three():
    return list(filter(lambda num: num % 2 == 0, range(1, 101)))


def four():
    return [x for x in range(1, 101) if x % 2 == 0]


print(timeit(three))

print(timeit(four))
