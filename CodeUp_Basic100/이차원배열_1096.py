N = int(input())
shape = [[0 for _ in range(19)] for _ in range(19)]

for _ in range(N):
    x, y = map(lambda re: int(re)-1, input().split())
    shape[x][y] = 1

for s in shape:
    print(*s)