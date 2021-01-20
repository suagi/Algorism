h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]
# board = [0 for _ in range(h)]
# for i in range(h):
#     board[i] = [0 for _ in range(w)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            board[x-1][y-1+i] = 1
    else:
        for j in range(l):
            board[x-1+j][y-1] = 1

for b in board:
    print(*b)
