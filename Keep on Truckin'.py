import sys
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030,
          5990, 6010, 7000]
mindis = input()
maxdis = input()
newlocs = input()
ways = 0
routes = [0]

def travel(curloc, ways, routes):
    del routes[len(routes)-1]
    poss = []
    for km in range(curloc + mindis, curloc + maxdis + 1):
        for m in motels:
            if km == m:
                poss.append(m)
    for i in poss:
        routes.append(i)
        
for i in range(newlocs):
    loc = int(sys.stdin.readline())
    print loc
    motels = motels + [loc]
motels.sort()

while len(routes) > 0:
    routes.sort()
    travel(max(routes), ways, routes)
    if 7000 in routes:
        ways += 1
        routes.remove(7000)
print ways
    
