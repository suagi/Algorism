# p. 321

S = input()
count = int(len(S) / 2)
front = S[0:count]
back = S[count:]
front_sum = 0
back_sum = 0

for i in range(count):
    front_sum += int(front[i])
    back_sum += int(back[i])

if front_sum == back_sum:
    result = 'LUCKY'
else:
    result = 'READY'

print(result)




