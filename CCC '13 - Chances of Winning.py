points = [0, 0, 0, 0]
rg = [3, 3, 3, 3]
games = [12, 13, 14, 23, 24, 34]

team = int(raw_input())
fin = int(raw_input())
for i in range(fin):
    line = raw_input().split()
    if int(line[2]) > int(line[3]):
        points[int(line[0])-1] += 3
    elif int(line[2]) < int(line[3]):
        points[int(line[1])-1] += 3
    elif int(line[2]) == int(line[3]):
        points[int(line[0])-1] += 1
        points[int(line[1])-1] += 1
    rg[int(line[0])-1] -= 1
    rg[int(line[1])-1] -= 1
    games.remove(int("".join(line[0:2])))

print points
print rg
print games

count = 3**(6-games)

def play(gm, poss, rag, points, count):
    if len(rag) == 1:
        points[int(gm[0])-1] += 3
        if points[team-1] == max(points) and points.count(max(points)) == 1:
            pass
        else:
            count -= 1
        points[int(gm[0])-1] -= 3
        points[int(gm[1])-1] += 3
        if points[team-1] == max(points) and points.count(max(points)) == 1:
            pass
        else:
            count -= 1
        points[int(gm[1])-1] -= 2
        points[int(gm[0])-1] += 1
        if points[team-1] == max(points) and points.count(max(points)) == 1:
            pass
        else:
            count -= 1
        return points
    else:
        return
