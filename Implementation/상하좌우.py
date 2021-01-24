# page. 110

N = int(input())
x, y = 1, 1

in_key = input().split()
for i in in_key:
    if y < N + 1 and i == "R":
        y += 1
    elif y > 1 and i == "L":
        y -= 1
    elif x < N + 1 and i == "D":
        x += 1
    elif x > 1 and i == "U":
        x -= 1
    else:
        continue

print(x, y)

print("---------- 다른풀이 ----------")

N = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x, y = nx, ny

print(x, y)