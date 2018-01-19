def is_prime(x):
    divisor = 2
    while divisor <= x**(1/2.0):
        if x % divisor == 0:
            return False
        divisor += 1
    return True

for j in range(int(raw_input())):
    a, b = map(int, raw_input().split())
    count = 0

    if a == 2:
        a += 1
        count += 1
    elif a % 2 == 0:
        a += 1
    elif a == 1:
        a += 2
        count += 1

    for i in range(a, b, 2):
        if is_prime(i):
            count += 1

    print count
    
