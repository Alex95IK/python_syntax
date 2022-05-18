my_list = [[1, 2, 3], ['a', 'b', 'c'], [12, 23, 45], [12, 13, 14], [20, 30, 40], [100, 200, 300]]

new_list = []

for x, y, *z in my_list:
    print(z)


print(new_list)
