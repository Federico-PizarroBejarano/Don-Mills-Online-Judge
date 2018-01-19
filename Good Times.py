zones = [["Ottawa", 0], ["Victoria", -3], ["Edmonton", -2], ["Winnipeg", -1], \
         ["Toronto", 0], ["Halifax", 1], ["St. John's", 130]]

time = raw_input()

for i in zones:
    a = "0"*(4 - len(time)) + time
    if i[1] != 130:
        a = int(str(i[1] + int(a[0:2])) + a[2:])
        if abs(a) != a:
            a = "0"*(4 - len(str(abs(a)))) + str(abs(a)) 
            a = str(24 - int(a[0:2])) + a[2:]
    if i[1] == 130:
        a = str(1 + int(a[0:2])) + str(int(a[2:]) + 30)
        a = "0"*(4 - len(str(abs(int(a))))) + str(abs(int(a)))
        if int(a[2:]) > 59:
            b = str(int(a[0:2]) + 1)
            if (int(a[2:]) - 60) > 0:
                a = b + "0"*(2 - len(str(int(a[2:]) - 60))) + str(int(a[2:]) - 60)
            else:
                a = b + "00"
    a = int(a)
    a = "0"*(4 - len(str(abs(a)))) + str(abs(a))
    if int(a) > 2359:
        a = str(int(a)-2400)
    b = []
    for j in range(len(a)):
        if a.count("0") == len(a):
            b += ["0"]
            break
        elif a[j] != "0":
            b = list(a[j:])
            break
    print (str("".join(b)) + " in " + i[0])
