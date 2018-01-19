conds = map(float, raw_input().split())
n = int(raw_input())

bonus = [[], [], []]
for i in range(n):
    cj, sj, pj = map(float, raw_input().split())
    bonus[0].append(cj)
    bonus[1].append(sj)
    bonus[2].append(pj)

squad = []
sums = [0, 0, 0]

for i in range(n):
    if len(squad) < 5:
        squad.append(i)
        for j in range(3):
            sums[j] += bonus[j][i]
    else:
        mb = min(sums)
        ma = [[0, 0, 0], 0]
        
        for pirate in range(5):
            tempsums = list(sums)
            for j in range(3):
                tempsums[j] -= bonus[j][squad[pirate]]
                tempsums[j] += bonus[j][i]
            if min(tempsums) > min(ma[0]):
                ma = [tempsums, squad[pirate]]
        if mb < min(ma[0]):
            squad.remove(ma[1])
            squad.append(i)
            sums = ma[0]
        print squad, sums

if (min(sums)*100)/conds[sums.index(min(sums))] > 100:
    print 100.0
else:
    print round((min(sums)*100)/conds[sums.index(min(sums))], 1) 

        
        
