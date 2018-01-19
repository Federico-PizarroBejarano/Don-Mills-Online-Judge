alph = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
num = int(raw_input())
line = list(raw_input())
for i in range(len(line)):
    if line[i] != " ":
        if line[i] == line[i].upper():
            line[i] = (alph[(alph.index(line[i].lower()) - num)%26]).upper()
        else:
            line[i] = alph[(alph.index(line[i].lower()) - num)%26]
        
print "".join(line)
