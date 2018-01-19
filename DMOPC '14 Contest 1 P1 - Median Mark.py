num = int(raw_input())
marks = []
for i in range(num):
    marks.append(int(raw_input()))

marks.sort()
if num%2 == 1:
    print marks[num/2]
else:
    print int(round((marks[num/2] + marks[num/2 - 1])/2))
