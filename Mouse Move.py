c, r = map(int, raw_input().split(" "))
orix = 0
oriy = 0
while 1 == 1:
    x, y = map(int, raw_input().split(" "))
    if x == 0 and y == 0:
        break
    if orix + x <= 0:
        orix = 0
    if oriy + y <= 0:
        oriy = 0
    if orix + x >= c:
        orix = c
    if oriy + y >= r:
        oriy = r
    if 0 < orix + x < c:
        orix += x
    if 0 < oriy + y < r:
        oriy += y
    print orix, oriy
