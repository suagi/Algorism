# 1063
A, B = map(int, input().split())
print(A > B and A or B)

# 1064
A, B, C = map(int, input().split())
D = A > B and B or A
print(C > D and D or C)

print(D if C > D else C)

# Bonus
N = int(input())
print("짝" if N % 2 == 0 else "홀")
print("홀" if N % 2 else "짝")