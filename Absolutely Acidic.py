freq = []
types = []
for i in range(int(raw_input())):
    b = int(raw_input())
    if b not in types:
        types += [b]
        freq += [0]
    freq[types.index(b)] += 1

if freq.count(max(freq)) > 1:
    diff = []
    for i in range(len(freq)):
        if freq[i] == max(freq):
            diff += [types[i]]
    print (max(diff) - min(diff))
else:
    big = types[freq.index(max(freq))]
    del types[freq.index(max(freq))]
    freq.remove(max(freq))
    if freq.count(max(freq)) > 1:
        diff = []
        for i in range(len(freq)):
            if freq[i] == max(freq):
                diff += [types[i]]
        print max(abs(big - min(diff)), abs(big - max(diff)))
    else:
        print abs(big - types[freq.index(max(freq))])


