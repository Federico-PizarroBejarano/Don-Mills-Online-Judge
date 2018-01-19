def check(x):
    if x == x.upper():
        return "dom"
    elif x == x.lower():
        return "rec"
    else:
        return "mix"

mom = raw_input()
dad = raw_input()
poss = []

for i in range(5):
    if check(mom[2*i:2*i + 2]) == "dom" or check(dad[2*i:2*i + 2]) == "dom":
        poss.append("dom")
    elif check(mom[2*i:2*i + 2]) == "rec" and check(dad[2*i:2*i + 2]) == "rec":
        poss.append("rec")
    else:
        poss.append("mix")

num = input()

for i in range(num):
    baby = raw_input()
    b = False
    for i in range(5):
        if check(baby[i]) != poss[i] and poss[i] != "mix":
            print "Not their baby!"
            b = True
            break
    if b == False:
        print "Possible baby."
