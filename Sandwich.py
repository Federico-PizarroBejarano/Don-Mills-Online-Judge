from sys import stdin
num = int(raw_input())
bn = stdin.read()
lyr = []
lyr2 = []
for i in xrange(num):
    if bn[i] == "0":
        lyr.append(i+1)
    else:
        lyr2.append(str(i+1))
print '\n'.join(map(str, lyr2[::-1]))
print '\n'.join(map(str, lyr))
