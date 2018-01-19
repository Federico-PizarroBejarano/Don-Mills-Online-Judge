dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
a = []
decode = ""
plain = raw_input()
cipher = raw_input()
message = raw_input()
for i in range(len(message)):
    if message[i] not in cipher:
        decode += "."
    else:
        decode += plain[cipher.index(message[i])]
print decode
