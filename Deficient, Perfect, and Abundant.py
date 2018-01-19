for i in range(int(raw_input())):
    num = float(raw_input())
    if num == 0 or num == 1:
        print "deficient"
        continue
    count = 0
    if num % 2 == 0:
        div = 1
    else:
        div = 2
    for i in xrange(1, int(num/2)+1, div):
        if int(num/i) == num/i:
            count += i
    if count < num:
        print "{} is a deficient number.".format(int(num))
    elif count == num:
        print "{} is a perfect number.".format(int(num))
    else:
        print "{} is an abundant number.".format(int(num))
