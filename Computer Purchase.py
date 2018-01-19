num = input()
values = []
names = []
for i in range(num):
    a = raw_input().split()
    names.append(a[0])
    values.append(2*int(a[1]) + 3*int(a[2]) + int(a[3]))
    
for i in range(2):
    if len(values) == 1:
        print names[0]
        break
    elif len(values) < 1:
        break
    elif values.count(max(values)) > 1:
        if len(names) == 2 and i == 0:
            print sorted(names)[0], "\n", sorted(names)[1]
            break
        sup = []
        for j in xrange(len(names)):
            if values[j] == max(values):
                sup.append(names[j])
        del values[names.index(sup[0])]
        names.remove(sup[0])
        print sorted(sup)[0]
    else:
        print names[values.index(max(values))]
        del names[values.index(max(values))]
        del values[values.index(max(values))]
