count = []
for i in range(int(input())):
    line = input().split()
    for i in line:
        if i[0] == i[0].upper():
            count.append([x for x in list(i) if x.isalpha()])             

for i in range(len(count)):
    print ("".join(count[i]))
