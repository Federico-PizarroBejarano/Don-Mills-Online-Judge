alph = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
key = list(raw_input().lower())
key[:] = [x for x in key if x in alph]
keyid = []
mess = list(raw_input().lower())
mess[:] = [x for x in mess if x in alph]
messlis = []

for i in range(len(key)):
    for le in range(len(mess[i::len(key)])):
        mess[i+len(key)*le] = alph[((alph.index(mess[i+len(key)*le]) + alph.index(key[i])))%26]
print str("".join(mess)).upper()
