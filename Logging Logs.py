days = input()
for j in range(days):
    trees = input()
    count = 0
    for i in range(trees):
        count += input()
    if count == 0:
        print "Weekend"
    else:
        print "Day {}: {}".format(j+1, count)
