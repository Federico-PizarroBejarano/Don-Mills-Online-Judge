def round3(x):
    x *= 10000
    if int(str(x)[-1]) >= 5:
        x += 10
    x = int(x)
    x -= int(str(x)[-1])
    x /= 10000.0
    if int(x) != x:
        x = str(x) + "0"*(4 - len(str(x)[str(x).index("."):]))
    else:
        x = str(int(x)) + ".000"
    return x

mark = 0
stdn = 0
for i in range(int(raw_input())):
    mark += int(raw_input())
    stdn += 1

for i in range(int(raw_input())):
    mark += int(raw_input())
    stdn += 1
    print round3(mark/float(stdn))
