from sys import exit

a = True
vowels = ("a", "e", "i", "o", "u", "y")
while a:
    word = raw_input()
    if word == "quit!":
        a == False
        exit()
    else:
        b = False
        if word[-2:] == "or" and len(word) > 4 and word[-3] not in vowels:
            print word[:-1] + "ur"
            b = True
        if b == False:
            print word
