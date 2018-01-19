from sys import exit

word = raw_input()
awords = []
if word.count("B") != word.count("S"):
    exit()
elif word.count("B") + word.count("S") + word.count("A") + word.count("N")\
    != len(word):
    exit()
else:
    for i in range(len(word)):
        if word[i] == "B":
            b = 0
            s = 0
            for j in range(len(word[i + 1:])):
                if word[i + 1:][j] == "S":
                    print b, s
                    if b == s:
                        awords += [word[i:j+i+2]]
                        awords += [word[j+2+i:]]
                        awords += [word[:i]]
                        print awords
                        exit()
                    else:
                        s += 1
                if word[i + 1:][j] == "B":
                    b += 1
print awords
""" if word[:i] != "" and word[:i][-1] != "N":
                            print "NO1"
                            exit()
                        elif word[:i] != "":
                            awords += [word[:i-1]]
                        if word[j+i+2:] != "" and word[j+i+2:][0] != "N":
                            print "NO2"
                            exit() 
                        elif word[j+1+i:] != "":
                            awords += word[j+2+i:]"""
