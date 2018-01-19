start = int(raw_input())
end = int(int(raw_input())**(1/3.0)) + 2
c = 0
if start**(1/3.0) == int(start**(1/3.0)):
    start **= (1/3.0)
else:
    start **= (1/3.0)
    start = int(start)
    start += 1

for i in xrange(int(start), int(end)):
    if i ** (3/2.0) == int(i ** (3/2.0)):
        c += 1
        print i**3
print c
    
