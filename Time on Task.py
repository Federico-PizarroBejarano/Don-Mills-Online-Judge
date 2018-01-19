tm = int(raw_input())
num = int(raw_input())
chores = []
mts = 0
for i in xrange(num):
    chores.append(int(raw_input()))
chores.sort()
for i in range(num):
    mts += chores[i]
    if mts > tm:
        print i
        break
