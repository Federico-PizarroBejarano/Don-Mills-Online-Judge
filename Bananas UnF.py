words = []
yn = []
a = True
while a:
    meh = raw_input()
    if meh == "X":
        a = False
    else:
        words.append(meh)

for word in words:
    if word[0] == "B" and word[-1] != "S" or word[0] != "B" and word[-1] == "S":
        yn.append("NO")
        continue
    if word[0] == "B" and word[-1] == "S":
        word = word[1:len(word)-1]
    if word[0] != "A" and word[-1] != "A":
        yn.append("NO")
        continue
    wor = word + "N"
    fml = [wor[i:i + 2] for i in range(0, len(wor), 2)]
    damn = True
    for i in range(len(word)):
        if word[i] != "A" and word[i] != "N":
            yn.append("NO")
            damn = False
            break
        for j in fml:
            if j != "AN":
                yn.append("NO")
                damn = False
                break
        if damn == False:
            break
    if damn == True:
        yn.append("YES")
for i in yn:
    print i
            
