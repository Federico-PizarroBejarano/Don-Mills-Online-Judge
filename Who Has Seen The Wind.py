h = int(raw_input())
m = int(raw_input())
for t in xrange(1, m + 1):
    if t*((-6*(t**3)) + (h*(t**2)) + (2*t) + 1) < 1:
        print "The balloon first touches ground at hour: \n6"
        break
    elif t == m:
        print "The balloon does not touch ground in the given time."
