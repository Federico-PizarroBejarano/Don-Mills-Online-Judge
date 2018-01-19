from math import log
a = input()
end = []
for i in range(a):
    num = input()
    if num == 0:
        end.append("0000")
        continue
    binnum = ""
    lognum = int(log(num, 2))
    for i in range(lognum + 1)[::-1]:
        if num >= 2**i:
            binnum += "1"
            num -= 2**i
        else:
            binnum += "0"
    while True:
        if len(binnum) % 4 != 0:
            binnum = "0" + binnum
        else:
            break
    end.append(" ".join([binnum[i:i + 4] for i in range(0, len(binnum), 4)]))
for i in end:
    print i
