from math import sqrt
def is_prime(x):
    divisor = 2
    while divisor <= sqrt(x):
        if x % divisor == 0:
            return False
        divisor += 1
    return True

a = input()
b = True

while b:
    if a == 1:
        a = 2
        b = False
    if is_prime(a) == False:
        a += 1
    else:
        b = False
print a
