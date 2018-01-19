st = int(raw_input())
c = st + 1
while 1 == 1:
    d = ""
    for i in str(c):
        if str(c).count(i) > 1:
            d = c + 1
    if d == "":
        print c
        break
    else:
        c = d
        
