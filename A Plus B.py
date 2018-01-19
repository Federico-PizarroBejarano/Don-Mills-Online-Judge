number = input()
sums = []

for i in range(number):
    a, b = raw_input().split(" ")
    sums.append(int(a) + int(b))
for i in sums:
    print i
