def find(x):
    for i in range(5):
        if x in fir[i]:
            return [i, fir[i].index(x)]
            
fir = [["A", "B", "C", "D", "E", "F"], ["G", "H", "I", "J", "K", "L"],
        ["M", "N", "O", "P", "Q", "R"], ["S", "T", "U", "V", "W", "X"],
        ["Y", "Z", " ", "-", ".", "/"]]
word = raw_input() + "/"
total = 0
movesy = [0]
movesx = [0]

for i in word:
    desy, desx = find(i)
    movesy.append(desy)
    movesx.append(desx)

for i in range(len(movesy) - 1):
    total += abs(movesy[i] - movesy[i+1])

for i in range(len(movesx) - 1):
    total += abs(movesx[i] - movesx[i+1])
print total

