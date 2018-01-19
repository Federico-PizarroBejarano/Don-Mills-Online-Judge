v = int(raw_input())
e = int(raw_input())

g = [[] for x in xrange(v)]

for i in range(e):
    ns, af = map(int, raw_input().split())
    if af not in g[ns-1]:
        g[ns-1].append(af)

def dfs(x):
    seen = [x]
    q = []
    path = [[] for i in xrange(v)]
    
    path[x-1] = [x]
        
    condition = True
    c = x
    while condition == True:
        for i in range(len(g[c-1])):
            #print "p1", path, c
            path[g[c-1][i]-1] += [x for x in (list(path[c-1]) + [g[c-1][i]]) if x not in path[g[c-1][i]-1]]
            #print "p2", path, c
            if g[c-1][i] not in seen:
                q.append(g[c-1][i])
                seen.append(g[c-1][i])
            #path[g[c-1][i]-1].append(g[c-1][i])
            elif g[c-1][i] in path[c-1]:
                return False, seen
                condition = False
        #print seen, q, c
        if len(q) != 0:
            c = q[-1]
            del q[-1]
        else:
            return True, seen
            condition = False
seen = []
for i in range(v):
    if i+1 not in seen:
        ev, s = dfs(i+1)
        if ev == False:
            print "N"
            g = "FUCKED"
            seen += [x for x in s if x not in seen]
            break
if g != "FUCKED":
    print "Y"
