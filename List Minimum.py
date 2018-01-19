times = input()
items = []

for i in range(times):
    number = input()
    items.append(number)

for i in range(len(items)):
    print min(items)
    del(items[items.index(min(items))])
