adj = input()
nouns = input()
ladj = []
lnouns = []

for i in range(adj):
    a = raw_input()
    ladj.append(a)
for i in range(nouns):
    b = raw_input()
    lnouns.append(b)

for i in ladj:
    for j in lnouns:
        print i, "as", j
