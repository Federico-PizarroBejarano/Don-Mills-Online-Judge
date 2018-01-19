fir = []
sec = []
a = input()
num = int(a/2.0 + .5)
n = 0

if a >= 5:
	fir = [1]*5
	sec = [1]*(a - 5)
else:
	fir = [1]*a

while len(fir) >= num:
    del fir[0]
    sec.append(1)
    n += 1
print n
