n = int(raw_input())
kc = map(int, raw_input().split())

k = []
p = []
s = []
t = []

for i in range(n):
    kj, pj, sj, tj = map(int, raw_input().split())
    k.append(kj)
    p.append(pj)
    s.append(sj)
    t.append(tj)

tleft = max(s)

for i in range(n):
    if t[i]*kc[k[i]-1] + tleft <= 180:
        print 10-p[i]
    else:
        print "The kemonomimi are too cute!"
    
    
