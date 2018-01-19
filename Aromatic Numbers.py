rom = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
num = raw_input()
fin = 0
while len(num) > 0:
    if len(num) > 2:
        if rom[num[1]] < rom[num[3]]:
            fin += -(int(num[0])*rom[num[1]])
            num = num[2:]
        else:
            fin += int(num[0])*rom[num[1]]
            num = num[2:]
    else:
        fin += int(num[0])*rom[num[1]]
        num = num[2:]
print fin
