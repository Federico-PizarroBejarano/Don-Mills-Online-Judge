from sys import exit
mxw = int(raw_input())
num = int(raw_input())
cars = []
for i in xrange(num):
    cars.append(int(raw_input()))
    if i < 4:
        if sum(cars) > mxw:
            print i
            exit()
    else:
        if sum(cars[i-3:]) > mxw:
            print i
            exit()
print num
        

