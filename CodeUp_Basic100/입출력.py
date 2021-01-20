# 1001
print("Hello")

# 1002
print("Hello World")

# 1003
print("Hello\nWorld")

# 1004
print("\'Hello\'")

# 1005
print('\"Hello World\"')

# 1006
print('\"!@#$%^&*\"')

# 1007
print('\"C:\Download\hello.cpp\"')

# 1008
print("┌┬┐")
print("├┼┤")
print("└┴┘")

# 1010
print(int(input("정수를 입력: ")))

# 1011
print(str(input("문자를 입력: ")))

# 1012
print(float(input("실수를 입력: ")))

# 1013
A, B = map(int, input("정수 두개를 공백으로 입력: ").split())
print(A, B)

# 1014
A, B = input("문자 두개를 공백으로 입력: ").split()
print(B, A)

# 1015
print(round(float(input("실수를 입력: ")), 2))

# 1017
N = int(input("정수를 입력: "))
print(N, N, N)

# 1018
T, M = input("시:분 입력: ").split(":")
print("{}:{}" .format(T, M))

# 1019
Y, M, D = input("YYYY.MM.DD: ").split(".")
if len(M) == 1:
    M = "0" + M
if len(D) == 1:
    D = "0" + D
print("{}.{}.{}" .format(Y, M, D))

# 1020
resident_number = input("주민등록번호: ").replace("-", "")
print(resident_number)

# 1021
print(input("단어를 입력: "))

# 1022
print(input("문장을 입력: "))

# 1023
A, B = input("실수를 입력: ").split(".")
print(A)
print(B)

# 1024
keyword = input("단어를 입력: ")
for i in keyword:
    print("'{}'" .format(i))

# 1025
number = input("정수를 입력: ")
count = len(number)
for i in number:
    i = i + "0" * (count - 1)
    count -= 1
    print("[{}]" .format(i))

# 1026
H, M, S = input("시:분:초 ").split(":")
print(M)

# 1027
Y, M, D = input("YYYY.MM.DD ").split(".")
if len(M) == 1:
    M = "0" + M
if len(D) == 1:
    D = "0" + D

print("{}-{}-{}" .format(D, M, Y))