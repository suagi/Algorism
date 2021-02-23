# p. 313

S = input()
count = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

result = (count // 2 + 1) if count % 2 else (count // 2)

print(result)