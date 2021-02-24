# p. 315

N, M = map(int, input().split())
ball = list(map(int, input().split()))
select = [0] * 11

result = 0

for b in ball:
    select[b] += 1

for i in select:
    N -= i
    result += i * N

print(result)