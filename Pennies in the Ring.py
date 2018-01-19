while 1 == 1:
    radius = input()
    if radius == 0:
        break
    else:
        points = radius*4 + 1
        loc = [radius, 0]
        perimx = []
        perimy = []
        while loc[0] != 0:
            loc[0] -= 1
            loc[1] += 1
            while 1 == 1:
                if loc[0] == 0:
                    break
                elif loc[0]**2 + loc[1]**2 <= radius**2:
                    perimy.append(loc[0])
                    perimx.append(loc[1])
                    loc[1] += 1
                else:
                    loc[1] -= 2
                    break
        for i in range(len(perimx)):
            if i == 0:
                points += (perimy[i])*4
            elif perimx[i] != perimx[i-1]:
                points += (perimy[i])*4

        print points
