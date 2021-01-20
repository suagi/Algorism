# 1093
N = int(input())
call = map(int, input().split())
member = [0 for _ in range(23)]
for i in call:
    member[i-1] += 1
print(*member)

# 1094
N = int(input())
call = list(map(int, input().split()))
call.reverse()
print(*call)

# 1095
N = int(input())
call = list(map(int, input().split()))
# call.sort()
# print(call[0])
print(min(call))
