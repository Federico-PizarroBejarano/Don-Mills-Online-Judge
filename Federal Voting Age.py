num = input()
for i in range(num):
    year, month, day = map(int, raw_input().split(" "))
    if year > 1989:
        print "No"
    elif year == 1989:
        if month > 2:
            print "No"
        elif month == 2:
            if day > 27:
                print "No"
            else:
                print "Yes"
        else:
            print "Yes"
    else:
        print "Yes"
