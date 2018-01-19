amod = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def ad(x):
    x = ("0"*(2-len(str(x)))) + str(x)
    return x
jump = int(raw_input())
big, small = raw_input().split()
year, month, day = map(int, big.split("/"))
hour, minu, second = map(int, small.split(":"))
print jump
print year, month, day, hour, minu, second

day += ((hour - jump)-(hour - jump)%24)/24
hour = (hour - jump)%24

print year, month, day, hour, minu, second
counter = month - 2

while 1:
    if day <= 0:
        day += amod[counter%12]
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
        counter -= 1
    else:
        break

print "{}/{}/{} {}:{}:{}".format(ad(year), ad(month), ad(day), ad(hour), ad(minu), ad(second))
#2011/03/04 01:00:01
#2011/02/30 01:00:01
