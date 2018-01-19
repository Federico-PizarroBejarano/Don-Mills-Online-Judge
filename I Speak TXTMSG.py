a = True
b = []
while a:
    item = raw_input()
    if item=="CU":
        b.append("see you")
        continue
    elif item==":-)":
        b.append("I'm happy")
        continue
    elif item==":-(":
        b.append("I'm unhappy")
        continue
    elif item==";-)":
        b.append("wink")
        continue
    elif item==":-P":
        b.append("stick out my tongue")
        continue
    elif item=="(~.~)":
        b.append("sleepy")
        continue
    elif item=="TA":
        b.append("totally awesome")
        continue
    elif item=="CCC":
        b.append("Canadian Computing Competition")
        continue
    elif item=="CUZ":
        b.append("because")
        continue
    elif item=="TY":
        b.append("thank-you")
        continue
    elif item=="YW":
        b.append("you're welcome")
        continue
    elif item=="TTYL":
        b.append("talk to you later")
        a = False
    else:
        b.append(item)
for i in b:
    print i
        
