from math import sqrt
while 1 == 1:
    pics = input()
    if pics == 0:
        break
    else:
        root = int(sqrt(pics))
        while 1 == 1:
            if pics % root != 0:
                root -= 1
            else:
                break
        for i in range(root, pics/2 + 1):
            if pics%i == 0:
                div1 = i
                break
        div2 = pics/div1
        peri = 2*div1 + 2*div2
        print "Minimum perimeter is {} with dimensions {} x {}".format(peri, div2, div1)
