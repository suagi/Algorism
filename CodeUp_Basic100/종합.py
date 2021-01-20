# # 1078
# N = int(input())
# sum = 0
# for i in range(0, N+1, 2):
#     sum += i
# print(sum)
#
# # 1079
# A = input().split()
# for i in A:
#     print(i)
#     if i == 'q':
#         break
#
# # 1080
# N = int(input())
# S = 0
# for i in range(1, N+1):
#     S += i
#     if S >= N:
#         print(i)
#         break
#
# # 1081
# N, M = map(int, input().split())
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         print(i, j)
#
# # 1082
# Hex_num = int(input(), 16)
# for i in range(1, 16):
#     print("{:X} * {:X} = {:X}".format(Hex_num, i, Hex_num * i))
#
# # 1083
# SYK = int(input())
# for i in range(1, SYK+1):
#     print(i if i % 3 else "X", end=" ")
#
# print("")
# # 1084
# count = 0
# R, G, B = map(int, input().split())
# for r in range(R):
#     for g in range(G):
#         for b in range(B):
#             print(r, g, b)
#             count += 1
#
# print(count)
#
# # 1085
# h, b, c, s = map(int, input().split())
# print(str(round((h * b * c * s)/8/1024/1024, 1)) + " MB")
#
# # 1086
# r, g, b = map(int, input().split())
# print(round((r * g * b) / (8 * 1024 ** 2), 2), " MB")
#
# # 1087
# N = int(input())
# sum = 0
# for i in range(1, N):
#     if sum < N:
#         sum += i
#     else:
#         break
# print(sum)
#
# # 1088
# N = int(input())
# for i in range(1, N+1):
#     if i % 3 != 0:
#         print(i, end=" ")
#
# print("")
# # 1089
# a, d, n = map(int, input().split())
# number = [(a + d * i) for i in range(n)]
# print(number[-1])
#
# # 1090
# a, r, n = map(int, input().split())
# number = [(a * r ** i) for i in range(n)]
# print(number[-1])

a, r, n = map(int, input().split())
result = a
result_list = []
while n > len(result_list):
    result_list.append(result)
    result *= r
print(result_list[-1])

# 1091
a, m, d, n = map(int, input().split())
result = a
result_list = []
while n > len(result_list):
    result_list.append(result)
    result = result * m + d
print(result_list[-1])

# 1092
a, b, c = map(int, input().split())
day = 1
# day를 기간으로 나눴을 시 0 이외의 숫자가 나온다면 각 값의 배수가 아니기에
# day의 값을 증가시켜 a, b, c 각 값의 배수에 해당하는 수르 찾아낸다.
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)