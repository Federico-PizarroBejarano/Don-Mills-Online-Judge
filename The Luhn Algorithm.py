number = []
for i in range(5):
    stuff = raw_input()
    if 0 <= i <= 3:
        number.append(stuff + " ")
    else:
        number.append(stuff)
numb = ""
bb = []
for i in number:
    for j in i:
        numb += j

numb = numb.split(" ")

b = 1
secnum = []
firnum = []
fin = 0

for num in numb:
    for i in (str(num))[::-1]:
            b += 1
            if b % 2 == 0:
                secnum.append(int(i)*2)
                b = 0
            else:
                firnum.append(int(i))
    for i in secnum:
        for j in str(i):
            fin += int(j)

    for i in firnum:
        fin += int(i)
    a = (10 - int((str(fin))[-1]))
    if a == 10:
        a = 0
    bb.append(str(a))
    b = 1
    secnum = []
    firnum = []
    fin = 0
bb = [bb[i:i + 5] for i in range(0, len(bb), 5)]
for i in bb:
    if str("".join(i)) != "0" and str("".join(i)) != "1":
        print "".join(i)

