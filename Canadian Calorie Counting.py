dic1 = {1: 461, 2: 431, 3: 420, 4: 0}
dic2 = {1: 100, 2: 57, 3: 70, 4: 0}
dic3 = {1: 130, 2: 160, 3: 118, 4: 0}
dic4 = {1: 167, 2: 266, 3: 75, 4: 0}

burger = input()
side = input()
drink = input()
dessert = input()

print "Your total Calorie count is " + str(dic1[burger] + dic2[side] + dic3[drink] + dic4[dessert]) + "."
