ralp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
bnm = (("X", "V", "I"), ("C", "L", "X"), ("M", "D", "C"))

def con(rn, ralp):
    num = 0
    for dg in range(len(rn)):
        if len(rn[dg:]) > 1:
            if ralp[rn[dg:][0]] < ralp[rn[dg:][1]]:
                num += -(ralp[rn[dg]])
            else:
                num += ralp[rn[dg]]
        else:
            num += ralp[rn[dg]]
    return num

def back(rn, bnm):
    rmst = ""
    for i in range(len(rn)):
        if int(rn[i]) == 9:
            rmst += bnm[len(rn[i:]) - 1][2] + bnm[len(rn[i:]) - 1][0]
        elif 4 < int(rn[i]) < 9:
            rmst += bnm[len(rn[i:]) - 1][1] + (bnm[len(rn[i:]) - 1][2])*(int(rn[i])-5)
        elif int(rn[i]) == 4:
            rmst += bnm[len(rn[i:]) - 1][2] + bnm[len(rn[i:]) - 1][1]
        else:
            rmst += (bnm[len(rn[i:]) - 1][2])*(int(rn[i]))
    return rmst

for i in xrange(int(raw_input())):
    rom = raw_input()[0:-1].split("+")
    a = 0
    for rn in xrange(2):
        a += con(rom[rn], ralp)
    if a > 1000:
        print "+".join(rom) + "=CONCORDIA CUM VERITATE"
    elif a == 1000:
        print "+".join(rom) + "=M"
    else:
        print "+".join(rom) + "=" + back(str(a), bnm)
        
