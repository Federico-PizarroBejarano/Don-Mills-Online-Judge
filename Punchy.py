a = 0
b = 0
stva = {"A":a, "B": b}

while 1==1:
    ins = raw_input().split()
    if ins[0] == "7":
        break
    elif  ins[0] == "1":
        stva[ins[1]] = int(ins[2])
    elif  ins[0] == "2":
        print stva[ins[1]]
    elif  ins[0] == "3":
        stva[ins[1]] = stva[ins[1]] + stva[ins[2]]
    elif  ins[0] == "4":
        stva[ins[1]] = stva[ins[1]] * stva[ins[2]] 
    elif  ins[0] == "5":
        stva[ins[1]] = stva[ins[1]] - stva[ins[2]] 
    elif  ins[0] == "6":
        stva[ins[1]] = stva[ins[1]] / stva[ins[2]] 

