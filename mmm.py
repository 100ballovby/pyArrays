getLength = 6
items = [1, 2, 3, 4, 5, None, None]
element = 3
for i in range(getLength, 0, -1):
    items[i] = items[i-1]

items[0] = element
print(items)

