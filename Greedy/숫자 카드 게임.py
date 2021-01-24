
# page. 96

N, M = map(int, input().split())
NM = [0 for i in range(N)]
result = 0
for j in range(N):
    NM[j] = list(map(int, input().split()))

for x in range(N):
    for y in range(M):
        result = min(result, NM[x][y])
    result = max(result, NM[x][y])

print(result)

print("---------- 다른풀이 ----------")

N, M = map(int, input().split())
result = 0
for x in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)