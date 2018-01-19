n, m = map(int, raw_input().split())
d = {}

for i in xrange(m):
    u, v, w = map(int, raw_input().split())
    if u not in d:
        d[u] = []
    if v not in d:
        d[v] = []
    d[u].append([v, w])
    d[v].append([u, w])

boxed = [1]
dis = [0]

seen = []
temp = []
current = 1

done = []

condition = True

while condition == True:
    cond2 = True
    ids = []
    for i in range(len(d[current])):
        if d[current][i][0] not in boxed:
            if d[current][i][0] in seen and \
               (d[current][i][1]+dis[boxed.index(current)]) < temp[seen.index(d[current][i][0])]:
                seen.append(d[current][i][0])
                temp.append(d[current][i][1]+dis[boxed.index(current)])
                cond2 = False
            elif d[current][i][0] not in seen:
                seen.append(d[current][i][0])
                temp.append(d[current][i][1]+dis[boxed.index(current)])
                cond2 = False
                
    if cond2 == True and len(seen) == 0:
        condition = False
    else:
        mpd = [seen[temp.index(min(temp))], min(temp)] 
        boxed.append(mpd[0])
        dis.append(mpd[1])
        current = mpd[0]
        ID = seen.index(mpd[0])
        del seen[ID]
        del temp[ID]

            
for i in xrange(n):
    if i+1 in boxed:
        print dis[boxed.index(i+1)]
    else:
        print -1
