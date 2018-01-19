x = map(int, raw_input().split())
y = map(int, raw_input().split())

def knhop(x):
    adj = []
    if x[0] + 1 < 9 and x[1] + 2 < 9:
        adj.append([x[0]+1, x[1]+2])
    if x[0] + 2 < 9 and x[1] + 1 < 9:
        adj.append([x[0]+2, x[1]+1])
    if x[0] + 2 < 9 and x[1] - 1 > 0:
        adj.append([x[0]+2, x[1]-1])
    if x[0] + 1 < 9 and x[1] - 2 > 0:
        adj.append([x[0]+1, x[1]-2])
    if x[0] - 1 > 0 and x[1] - 2 > 0:
        adj.append([x[0]-1, x[1]-2])
    if x[0] - 2 > 0 and x[1] - 1 > 0:
        adj.append([x[0]-2, x[1]-1])
    if x[0] - 2 > 0 and x[1] + 1 < 9:
        adj.append([x[0]-2, x[1]+1])
    if x[0] - 1 > 0 and x[1] + 2 < 9:
        adj.append([x[0]-1, x[1]+2])
    return adj

seen = [x]
dos = [0]
q = []
dsq = []

condition = True
c = x
d = 1

while condition == True:
    adjp = knhop(c)
    for i in range(len(adjp)):
        if adjp[i] not in seen:
            q.append(adjp[i])
            dsq.append(d)
            dos.append(d)
            seen.append(adjp[i])
    #print seen, "--", dos, "--",q,"--", c,"--", d,"--", adjp
    if y in seen:
        print dos[seen.index(y)]
        break
    if len(q) != 0:
        c = q[0]
        del q[0]
        d = dsq[0] + 1
        del dsq[0]
    else:
        condition = False
