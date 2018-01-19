g = [[6],[6],[6,4,5,15],[6,3,5],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],\
     [9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17]]
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def bfs(x, y):
    seen = [x]
    dos = [0]
    q = []
    dsq = []

    condition = True
    c = x
    d = 1
    while condition == True:
        for i in range(len(g[f.index(c)])):
            if g[f.index(c)][i] not in seen:
                q.append(g[f.index(c)][i])
                dsq.append(d)
                dos.append(d)
                seen.append(g[f.index(c)][i])
        if y in seen:
            return dos[seen.index(y)]
            break
        if len(q) != 0:
            c = q[0]
            del q[0]
            d = dsq[0] + 1
            del dsq[0]
        else:
            condition = False
    if y not in seen:
        return "Not connected"

def bfs2(x):
    seen = [x]
    dos = [0]
    q = []
    dsq = []

    condition = True
    c = x
    d = 1
    while condition == True:
        for i in range(len(g[f.index(c)])):
            if g[f.index(c)][i] not in seen:
                q.append(g[f.index(c)][i])
                dsq.append(d)
                dos.append(d)
                seen.append(g[f.index(c)][i])
        if len(q) != 0:
            c = q[0]
            del q[0]
            d = dsq[0] + 1
            del dsq[0]
        else:
            condition = False
    return dos.count(2)

condition = True

while condition == True:
    cmd = raw_input()
    if cmd == 'q':
        condition = False
    elif cmd == 'n':
        x = int(raw_input())
        print len(g[f.index(x)])
    elif cmd == 'i':
        x = int(raw_input())
        y = int(raw_input())
        if x not in f:
            f.append(x)
            g.append([])
        if y not in f:
            f.append(y)
            g.append([])
        if y not in g[f.index(x)]:
            g[f.index(x)].append(y)
            g[f.index(y)].append(x)
    elif cmd == 'd':
        x = int(raw_input())
        y = int(raw_input())
        g[f.index(x)].remove(y)
        g[f.index(y)].remove(x)
    elif cmd == 's':
        x = int(raw_input())
        y = int(raw_input())
        print bfs(x, y)
    elif cmd == 'f':
        x = int(raw_input())
        print bfs2(x)
        
