snl = {54: 19, 90: 48, 99: 77, 9: 34, 40: 64, 67: 86}

pos = 1
while 1 == 1:
    mov = input()
    if mov not in range(2, 13):
        print "You Quit!"
        break
    elif (pos + mov) in snl.keys():
        pos = snl[pos+mov]
    elif (pos + mov) < 100:
        pos += mov 
    elif (pos + mov) == 100:
        print "You are now on square 100"
        print "You Win!"
        break
    print "You are now on square {}".format(pos)
        
