from sys import stdin
times = input()
items = []
a = stdin.read().split("\n")
a = map(int, a[:len(a)-1])
a.sort()
for i in a:
    print i
