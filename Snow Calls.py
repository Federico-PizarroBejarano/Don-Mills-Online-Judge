trans = {"A": 1, "B": 1,"C": 1,"D": 2,"E": 2,"F": 2,"G": 3,"H": 3,\
         "I": 3,"J": 4,"K": 4,"L": 4,"M": 5,"N": 5,"O": 5,"P": 6,\
         "Q": 6,"R": 6,"S": 6,"T": 7,"U": 7,"V": 7,"W": 8,"X": 8,\
         "Y": 8,"Z": 8,}
num = input()

for i in range(num):
    tele = list(raw_input())
    tele[:] = [x for x in tele if x != "-"]
    tele[:] = tele[:10]
    tele = tele + ["0"]*(10-len(tele))
    for ob in range(10):
        tele[ob] = str(tele[ob])
        if tele[ob].isalpha():
            tele[ob] = str(trans[tele[ob]]+1)
    first = tele[0:3]
    sec = tele[3:6]
    thir = tele[6:]
    done = "".join(first) +"-" + "".join(sec) + "-" + "".join(thir)
    print done
            
