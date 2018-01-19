a = input()
b = input()
c = input()
d = input()
s = input()
Nikky = (a-b)*(s/(a+b))
e = s - ((s/(a+b))*(a+b))
steps1 = tuple([1]*a + [-1]*b)
for i in range(e):
    Nikky += steps1[i]

Byron = (c-d)*(s/(c+d))
e = s - ((s/(c+d))*(c+d))
steps2 = tuple([1]*c + [-1]*d)
for i in range(e):
    Byron += steps2[i]
    
if abs(Nikky) > abs(Byron):
    print "Nikky"
elif abs(Nikky) < abs(Byron):
    print "Byron"
else:
    print "Tied"
    
