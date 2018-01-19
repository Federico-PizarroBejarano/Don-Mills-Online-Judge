def findlen(fir, sec):
    return float(((fir[0] - sec[0])**2 + (fir[1] - sec[1])**2)**(1/2.0))

for i in range(int(raw_input())):
    a = map(int, raw_input().split())
    a, b, c = [a[i:i + 2] for i in range(0, len(a), 2)]

    perimeter = str(findlen(a, b) + findlen(a, c) + findlen(b, c))
    area = str(abs((a[0]*(b[1] - c[1])+ b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))*(1/2.0)))

    if float(perimeter[perimeter.index("."):perimeter.index(".") + 4]) >= float(perimeter[perimeter.index("."):perimeter.index(".") + 3] + "5"):
        perimeter = (perimeter[:perimeter.index(".") + 2]) + str(int(perimeter[perimeter.index(".") + 2]) + 1)
    else:
        perimeter = perimeter[:perimeter.index(".") + 3]

    if float(area[area.index("."):area.index(".") + 4]) >= float(area[area.index("."):area.index(".") + 3] + "5"):
        area = (area[:area.index(".") + 2]) + str(int(area[area.index(".") + 2]) + 1)
    else:
        area = area[:area.index(".") + 3]

    print area + "0"*(2 - len(area[area.index(".") + 1:])), perimeter + "0"*(2 - len(perimeter[perimeter.index(".") + 1:]))
