briefs = {1:100, 2:500, 3:1000, 4:5000, 5:10000,
          6:25000, 7:50000, 8:100000, 9:500000, 10:1000000}
money = 0
num = input()
for i in range(num):
    rem = input()
    del briefs[rem]

offer = input()

for key in briefs:
    money += briefs[key]
money = money/len(briefs)
if offer > money:
    print "deal"
else:
    print "no deal"
