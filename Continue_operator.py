x = ''

while len(x) < 5:
    y = input('Please enter details: ')
    if y == 'o':
        continue
    if y == 'l':
        break
    x += y
else:
    print(x)
