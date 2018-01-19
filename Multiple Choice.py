from sys import stdin
times = input()
count = 0 
a = stdin.read().split("\n")
a = a[:len(a)-1]
a, b = [a[i:i + times] for i in range(0, len(a), times)]
for i in range(times):
    if a[i] == b[i]:
        count += 1
print count
