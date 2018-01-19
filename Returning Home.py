turns = []
streets = []
d = {"R":"LEFT","L":"RIGHT"}
a = True

while a:
    turn = raw_input()
    street = raw_input()
    turns.append(turn)
    if street == "SCHOOL":
        a = False
    else:
        streets.append(street)
    continue
streets = ["HOME"] + streets
for i in range(len(turns)):
    if i == len(turns) - 1:
        print "Turn {} into your {}.".format(d[turns[-(i+1)]], streets[-(i+1)])
    else:
        print "Turn {} onto {} street.".format(d[turns[-(i+1)]], streets[-(i+1)])
