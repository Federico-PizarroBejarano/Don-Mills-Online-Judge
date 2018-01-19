letter = []
binar = []
for i in range(int(raw_input())):
    let, bn = raw_input().split()
    letter += [let]
    binar += [bn]
seq = raw_input()
a = ""
fin = ""
for i in range(len(seq)):
    a += seq[i]
    if a in binar:
        fin += letter[binar.index(a)]
        a = ""
print fin
        
