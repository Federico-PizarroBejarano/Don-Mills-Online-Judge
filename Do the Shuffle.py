songs = ["A", "B", "C", "D", "E"]
while 1 == 1:
    button = input()
    times = input()
    if button == 4:
        break
    elif button == 1:
        for i in range(times):
            songs = songs[1:] + [songs[0]]
    elif button == 2:
        for i in range(times):
            songs = [songs[-1]] + songs[:-1]
    elif button == 3:
        for i in range(times):
            songs = [songs[1]] + [songs[0]] + songs[2:]
print " ".join(songs)
