first = ["le", "la", "les"]
second = ["moi", "toi", "nous", "vous", "lui", "leur"]
vowels = ("a", "e", "i", "o", "u", "y")

for i in range(int(raw_input())):
    line = raw_input().split(":")
    if line[0][-2:] == "er" and line[1][0:3] == " Tu" and line[1][-2:] == "s.":
        line = line[1][0:-2].split()
    else:
        line = line[1][0:-1].split()

    del line[0]

    line = " ".join(line).replace("l'", "le ").split()
    line = " ".join(line).replace("m'", "me ").split()
    line = " ".join(line).replace("t'", "te ").split()

    for i in range(len(line)):
        if line[i] == "me":
            line[i] = "moi"
        elif line[i] == "te":
            line[i] = "toi"
    n1 = []
    n2 = []
    n3 = []
    n4 = []

    for i in line:
        if i in first:
            n1.append(i)
        elif i in second:
            n2.append(i)
        elif i == "y":
            n3.append(i)
        elif i == "en":
            n4.append(i)

    newline = [line[-1].capitalize()] + n1 + n2 + n3 + n4

    for i in range(len(newline)-1):
        if newline[i] in ("le", "la") and newline[i+1][0] in vowels:
            newline[i] = "DEL"
            newline[i+1] = "l'" + newline[i+1]
        if newline[i] in ("me", "moi") and newline[i+1][0] in vowels:
            newline[i] = "DEL"
            newline[i+1] = "m'" + newline[i+1]
        if newline[i] in ("te", "toi") and newline[i+1][0] in vowels:
            newline[i] = "DEL"
            newline[i+1] = "t'" + newline[i+1]

    newline[:] = [x for x in newline if x != "DEL"]
        
    print "-".join(newline) + " !"
            
