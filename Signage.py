mess = ['WELCOME', 'TO', 'CCC', 'GOOD', 'LUCK', 'TODAY']
num = input()
while len(mess) > 0:
    w = num
    line = ""
    while len(mess) > 0:
        for i in range(len(mess)):
            if w >= len(".".join(mess)):
                line += ".".join(mess)
                mess = []
                w -= len(line)
                break
            elif w < len(".".join(mess[:i+1])):
                line += ".".join(mess[:i])
                mess = mess[i:]
                w -= len(line)
                break
        if w > 0 and line.count(".") > 0:
            a = [n for n in xrange(len(line)) if line.find('.', n) == n]
            line = list(line)
            count = 1
            while w > 0:
                for i in range(len(a)):
                    if w > 0:
                        line.insert(a[i]+count*i, ".")
                        w -= 1
                count += 1
                if w == 0:
                    break
            line = str("".join(line))
        if len(line) < 2:
            break
        if w > 0:
            line += "."*w
            w = 0
        print line
        break
