other_list = list('Some text')
other_list_02 = list(range(20, 31))


print(other_list)
print(other_list_02)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[2:7])
print(my_list[2:7:2])
print(my_list[-4:2:-1])

x = ['apple', 'yellow', 1, 2, 3, 4, 5, 6, 7, 8, 9, True, 2, 3.14, 2, 'yellow', 'end']

x.append('append')

x.insert(1, 'insert')

x.count(2)

x.sort()

x.reverse()

y = x.pop(0)

x.remove('yellow')

x.clear()

x.extend(['a', 'b', 'c'])

r = x.copy()
