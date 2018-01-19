num = input()
den = input()
midway = max((num, den)) / 2
if num == 0:
    print 0
elif den == 1:
    print num
else:
    for i in range(midway, 1, -1):
        if num%i == 0 and den%i == 0:
            num = num/i
            den = den/i
            break
    mixint = num/den
    fracnum = num-(mixint*den)
    if mixint == 0:
        print str(fracnum) + "/" + str(den)
    elif fracnum == 0:
        print mixint
    else:
        frac = str(fracnum) + "/" + str(den)
        mixint = str(mixint) + " "
        print mixint + frac    

