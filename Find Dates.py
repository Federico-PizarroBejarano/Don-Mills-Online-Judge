needz = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-")
censor = ("!", "?", ".", "\"", "\'", "@", "#", "$", "%", "^", "&", ";",\
          ":", "~", ",", "(", ")", "*")
amod = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

dates = []
rdates = []
for num in range(int(raw_input())):
    line = raw_input()

    for j in censor:
        line = line.replace(j, "")
    #print line
    line = line.split()
    #print line
    for i in range(len(line)):
        swag = list(line[i])
        swag[:] = (x for x in swag if x in needz)
        if list(line[i]) == swag:
            #print line[i]
            if len(swag) == 10 and swag.count("-") == 2:
                swag = line[i].split("-")
                #print swag
                if len(swag[0]) == 4 and len(swag[1]) == 2 and len(swag[2]) == 2:
                    dates.append(line[i])
for i in range(len(dates)):
    if 0 < int(dates[i][5:7]) < 13:
        if amod[int(dates[i][5:7])-1] >= int(dates[i][8:]):
            if int(dates[i][5:7]) == 2 and int(dates[i][8:]) == 29:
                if int(dates[i][0:4])%4 == 0 and int(dates[i][0:4]) != 1900:
                    print dates[i]
            else:
                print (dates[i])

        
                

