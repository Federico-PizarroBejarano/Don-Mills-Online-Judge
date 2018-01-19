a = ("I", "O", "S", "H", "Z", "X", "N")
b = raw_input()
for i in range(len(b)):
    if b[i] not in a:
        print "NO"
        break
    elif i == len(b) - 1:
        print "YES"
