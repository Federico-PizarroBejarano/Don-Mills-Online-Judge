slices = []
mush = []
for i in range(8):
    slices.append(int(raw_input()))
for i in range(8):
    mush.append(slices[(0 + i)%8] + slices[(1 + i)%8] + slices[(2 + i)%8] + slices[(3 + i)%8])
print max(mush)
