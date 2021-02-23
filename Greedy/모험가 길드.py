# p. 311

N = int(input())
user = list(map(int, input().split()))
user.sort()
team = 0
count = 0

for i in user:
    count += 1
    if count >= i:
        team += 1
        count = 0

print(team)