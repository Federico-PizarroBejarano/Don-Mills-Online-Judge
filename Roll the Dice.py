die1 = input()
die2 = input()
ways = 0

for i in range(die1):
    for j in range(die2):
        if (i+1) + (j+1) == 10:
            ways += 1
if ways != 1:
    print "There are {} ways to get the sum 10.".format(str(ways))
else:
    print "There is {} way to get the sum 10.".format(str(ways))
    
