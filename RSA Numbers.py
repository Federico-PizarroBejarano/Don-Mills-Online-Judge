beg = input()
end = input()
num = 0
for i in range(beg, end + 1):
    count = 0
    for j in range(1, i + 1):
        if i%j == 0:
            count += 1
    if count == 4:
        num += 1

print "The number of RSA numbers between {} and {} is {}".format(beg, end, num)
