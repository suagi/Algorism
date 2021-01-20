ant_house = [0 for _ in range(10)]
for i in range(10):
    ant_house[i] = list(map(int, input().split()))

x = 1
y = 1
while y < 9:
    if ant_house[x][y] == 0:
        ant_house[x][y] = 9
        y += 1
    elif ant_house[x][y] == 1:
        x += 1
        y -= 1
    else:
        ant_house[x][y] = 9
        break

for road in ant_house:
    print(*road)
