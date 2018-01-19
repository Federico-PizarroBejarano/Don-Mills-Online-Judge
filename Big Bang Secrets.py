alph = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
k = int(raw_input())
word = raw_input()
new = ""
for i in range(len(word)):
    new += alph[(alph.index(word[i].lower())) - (3*(i+1) + k)%26].upper()
print new
