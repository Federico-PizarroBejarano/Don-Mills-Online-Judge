alph = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

import sys
string = sys.stdin.readline().rstrip("\n")
leng = int(sys.stdin.readline().rstrip("\n"))

least = string[:leng]

for i in xrange(26):
    if alph[i] in string[:len(string)-leng+1]:
        ids = [n for n in xrange(len(string[:len(string)-leng+1])) if string[:len(string)-leng+1].find(alph[i], n) == n]
        break
for i in xrange(len(ids)):
    sub = string[ids[i]:ids[i]+leng]
    if sub<least:
        least = sub

sys.stdout.write(least + "\n")
