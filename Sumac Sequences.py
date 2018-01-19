m1 = int(raw_input())
m2 = int(raw_input())
c = 2
while 1 == 1:
    swag = abs(m1 - m2)
    m1 = m2
    m2 = swag
    c += 1
    
    if m2 > m1:
        print c
        break
