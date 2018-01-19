for i in xrange(int(raw_input())):
    order = []
    branch = []
    nextnum = 1
    for j in xrange(int(raw_input())):
        order.append(int(raw_input()))
    while 1:
        print order, branch
        if len(branch) == 0 and len(order) == 0:
            print "Y"
            break
        elif branch == []:
            if nextnum == order[-1]:
                del order[-1]
                nextnum += 1
                continue
            else:
                branch.append(order[-1])
                del order[-1] 
        elif branch != [] and order != []:
            if nextnum == branch[-1]:
                del branch[-1]
                nextnum += 1
                continue
            elif nextnum == order[-1]:
                del order[-1]
                nextnum += 1
                continue
            elif order[-1] > branch[-1]:
                print "N"
                break
            else:
                branch.append(order[-1])
                del order[-1] 
        else:
            if nextnum == branch[-1]:
                del branch[-1]
                nextnum += 1
                continue
            else:
                print "N"
                break
