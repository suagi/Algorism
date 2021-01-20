# 1071
A = map(int, input().split())
for i in A:
    if i == 0:
        break
    print(i)

# 1072
N = int(input())
for i in range(N):
    print(i + 1)

# 1073
A = map(int, input().split())
for i in A:
    if i == 0:
        break
    print(i)

B = map(int, input().split())
for i in B:
    if i != 0:
        print(i)
    continue

# 1074
N = int(input())
for i in range(N, 0, -1):
    print(i)

# 1075
N = int(input())
while N > 0:
    print(N - 1)
    N -= 1

M = int(input())
for i in range(M - 1, -1, -1):
    print(i)

# 1076
A = ord(input())
count = A - 96
for i in range(count):
    print(chr(i + 97), end=" ")

B = ord(input())
for i in range(97, B+1, 1):
    print(chr(i), end=" ")

# 1077
N = int(input())
for i in range(N + 1):
    print(i)