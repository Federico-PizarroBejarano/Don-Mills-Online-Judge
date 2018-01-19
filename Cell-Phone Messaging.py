trans = {"A": 1, "B": 1,"C": 1,"D": 2,"E": 2,"F": 2,"G": 3,"H": 3,\
         "I": 3,"J": 4,"K": 4,"L": 4,"M": 5,"N": 5,"O": 5,"P": 6,\
         "Q": 6,"R": 6,"S": 6,"T": 7,"U": 7,"V": 7,"W": 8,"X": 8,\
         "Y": 8,"Z": 8}
hits = {"A": 1, "B": 2,"C": 3,"D": 1,"E": 2,"F": 3,"G": 1,"H": 2,\
         "I": 3,"J": 1,"K": 2,"L": 3,"M": 1,"N": 2,"O": 3,"P": 1,\
         "Q": 2,"R": 3,"S": 4,"T": 1,"U": 2,"V": 3,"W": 1,"X": 2,\
         "Y": 3,"Z": 4}
a = True
while a:
    sec = 0
    ent = raw_input()
    ent = ent.upper()
    if ent == "HALT":
        a = False
    else:
        for i in range(len(ent)):
            sec += hits[ent[i]]
            if i > 0:
                if trans[ent[i]] == trans[ent[i-1]]:
                    sec += 2
            
    if ent != "HALT":
        print sec
