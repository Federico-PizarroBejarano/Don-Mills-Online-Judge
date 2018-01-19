for i in range(int(raw_input())):
    line = raw_input().split()
    for i in range(len(line)):
        if len(line[i]) == 4:
            line[i] = "****"
    print " ".join(line)
