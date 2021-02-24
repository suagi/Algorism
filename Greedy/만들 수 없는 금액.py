# p.314

N = input()
coin = list(map(int, input().split()))
coin.sort()
result = 1

for c in coin:
    if result < c:
        break
    result += c

print(result)

