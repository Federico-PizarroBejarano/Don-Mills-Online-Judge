mark = int(raw_input())
d = {}
for i in range(mark - 1):
    d[i + 1] = int(raw_input())
d2 = {}

for k in d:
	if d[k] != mark:
		d2[k] = d[k]
    
q = [[]]

def add(x, a, q, d2):
    for i in range(1, a):
        if sorted(x + [i]) not in q:
            a = False
            for j in sorted(x + [i]):
                if sorted(x + [i]).count(j) > 1:
                    a = True
                    break
                else:
                    for item in d2:
                        if d2[item] in sorted(x + [i]) and item not in sorted(x + [i]):
                            a = True
                            break
            if not a:
                q += [sorted(x + [i])]

for i in range(1, mark):
    bs = [x for x in q if len(list(x)) == i-1]
    for j in bs:
        add(j, mark, q, d2)

print q
print len(q)
