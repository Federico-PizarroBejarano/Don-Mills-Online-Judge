n, m, x, y = map(int, raw_input().split())

g = []
p = range(1,n+1)

for i in range(n):
    g.append([])
    
for i in range(m):
    i, j = map(int, raw_input().split())
    g[i-1].append(j)
    g[j-1].append(i)

def bfs(x, y):
    seen = [x]
    dos = [0]
    q = []
    dsq = []

    condition = True
    c = x
    d = 1
    while condition == True:
        for i in range(len(g[p.index(c)])):
            if g[p.index(c)][i] not in seen:
                q.append(g[p.index(c)][i])
                dsq.append(d)
                dos.append(d)
                seen.append(g[p.index(c)][i])
        #print seen, dos, q, c, d
        if y in seen:
            return "GO SHAHIR!"
            break
        if len(q) != 0:
            c = q[0]
            del q[0]
            d = dsq[0] + 1
            del dsq[0]
        else:
            condition = False
    if y not in seen:
        return "NO SHAHIR!"

print bfs(x, y)

