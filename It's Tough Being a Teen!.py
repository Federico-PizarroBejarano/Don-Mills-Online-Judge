after = [1, 1, 2, 3, 3]
before = [7, 4, 1, 4, 5]

while 1 == 1:
    a = input()
    b = input()
    if a == 0:
        break
    else:
        after += [a]
        before += [b]

comp = []
while len(comp) < 7:
    count = 0
    if len(comp) == 7:
        break
    for i in range(1, 8):
        if len(comp) == 7:
            break
        if (i not in before) and (i not in comp):
            comp += [i]
            if i in after:
                for j in range(len(after)):
                    if after[j] == i:
                        before[j] = "del"
                        after[j] = "del"
                break
        else:
            count += 1
    if count == 7:
        print "Cannot complete these tasks. Going to bed."
        break
if len(comp) == 7:
    for i in range(7):
        print comp[i], 
