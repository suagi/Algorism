S = input()
result = 0
for i in range(len(S)):
    if int(S[i]) <= 1 or result <= 1:
        result += int(S[i])
    else:
        result *= int(S[i])

print(result)

print("---------- 다른풀이 ----------")

S = input()
result = int(S[0])
for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)