# p. 322

S = input()
A = [ord(s) for s in S]
A.sort()
sum = 0
key = []
for a in A:
    if a > 57:
        key += chr(a)
    else:
        sum += int(chr(a))

key.append(str(sum))
print("".join(key))
print(" ".join(key))