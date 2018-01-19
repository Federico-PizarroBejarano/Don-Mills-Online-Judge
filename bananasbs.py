from sys import exit

words = []
yn = []
while 1 == 1:
    meh = list(raw_input())
    if meh == ["X"]:
        break
    else:
        words.append(meh)

for word in words:
    for i in range(len(word)):
        a = True
        if word[i] == "B":
            a = False
            for j in range(len(word[::-1])):
                if word[::-1][j] == "S":
                    word[i] = "del"
                    word[len(word) - 1 - j] = "del"
                    a = True
                    break
            if a == False:
                yn += ["NO"]
                exit()
    word[:] = [x for x in word if x != "del"]
    word = ["N"] + word
    fml = [word[i:i + 2] for i in range(0, len(word), 2)]
    for i in fml:
        if i != ["N", "A"]:
            yn += ["NO"]
            exit()

    yn += ["YES"]
print yn
