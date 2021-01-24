# page. 115

start = input()
movement = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
field = [0 for _ in range(8)]
for i in range(8):
    field[i] = [0 for _ in range(8)]

for x in range(8):
    for y in range(8):
        field[x][y] = chr(97+y) + str(x+1)
        if field[x][y] == start:
            set_x = x
            set_y = y

count = 0
for m in movement:
    re_x = set_x + m[0]
    re_y = set_y + m[1]

    if 0 <= re_x < 8 and 0 <= re_y < 8:
        count += 1

print(count)