verses = input()
poem = []
for i in range(verses):
    stanza = []
    for i in range(4):
        line = raw_input().split(" ")[-1].lower()
        back = line[::-1]
        if len([i for i in line if i in ("a", "e", "i", "u", "o")]) > 0:
            for j in range(len(back)):
                if back[j] in ("a", "e", "i", "u", "o"):
                    line = back[:j+1]
                    line = line[::-1]
                    break
        stanza.append(line)
    poem.append(stanza)

for i in poem:
    if all(x==i[0] for x in i):
        print "perfect"
    elif all(x==i[::2][0] for x in i[::2])and all(x==i[1::2][0] for x in i[1::2]):
        print "cross"
    elif all(x==i[:2][0] for x in i[:2]) and all(x==i[2:][0] for x in i[2:]):
        print "even"
    elif all(x==i[::3][0] for x in i[::3]) and all(x==i[1:3][0] for x in i[1:3]):
        print "shell"
    else:
        print "free"
    
