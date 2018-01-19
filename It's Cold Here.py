cities = []
temps = []
while 1 == 1:
    city, temp = raw_input().split(" ")
    cities.append(city)
    temps.append(int(temp))
    if city == "Waterloo":
        break
print cities[temps.index(min(temps))]
