A = [0 for i in range(19)]
for a in range(19):
    A[a] = list(map(int, input().split()))

N = int(input())
for _ in range(N):
    x, y = map(lambda num: int(num)-1, input().split())
    for i in range(19):
        A[i][y] = 1 if A[i][y] == 0 else 0
        A[x][i] = 1 if A[x][i] == 0 else 0

for x in A:
    print(*x)
