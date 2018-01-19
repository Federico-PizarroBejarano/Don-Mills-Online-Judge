a = True
infile = []
while a:
    stuff = raw_input()
    if stuff == "EOF":
        a = False
    else:
        infile.append(stuff)
taken = 0
take = 0
serve = 0

for i in infile:
    if i.isalpha():
        if i == "TAKE":
            take += 1
            taken += 1
            if taken >= 999:
                taken = 0
            serve += 1
        elif i == "SERVE":
            serve -= 1
        elif i == "CLOSE":
            print take, serve, taken
            take = 0
            serve = 0
    else:
        taken += int(i)
