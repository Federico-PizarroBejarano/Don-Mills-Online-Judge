def round2(x):
    x = list(str(x))
    for i in range(len(x)):
        if x[i] == ".":
            if len(x[i:i+4]) <= 3:
                   return float("".join(x))
            x = x[:i+4]
            break
    if int(x[-1]) >= 5:
        x = list(str(float("".join(x)) + 0.01))
    x = x[:-1]
    return float("".join(x))

day = input()
eve = input()
week = input()
a = 100
b = 250
if day < 100:
    a = day
    b = day
elif day < 250:
    b = day

planA = (day-a)*.25 + eve*.15 + week*.20
planB = (day-b)*.45 + eve*.35 + week*.25

planA = round2(planA)
planB = round2(planB)

print "Plan A costs", planA
print "Plan B costs", planB

if planA == planB:
    print "Plan A and B are the same price."
elif planA < planB:
    print "Plan A is cheapest."
elif planA > planB:
    print "Plan B is cheapest."

