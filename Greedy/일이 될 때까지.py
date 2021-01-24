N, K = map(int, input().split())
count = 0
while N != 1:
    if K == 1:
        count = N - K
        break
    elif N % K == 0:
        N = N // K
        count += 1
    else:
        N -= 1
        count += 1

print(count)

print("---------- 다른풀이 ----------")
print("큰 수를 처리할때")

N, K = map(int, input().split())
count = 0
A = (N // K) * K
count += (N - A)

while A != 1:
    if K == 1:
        count = N - K
        break
    A = A // K
    count += 1

print(count)
