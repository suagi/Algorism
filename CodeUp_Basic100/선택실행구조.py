# 1065
Number = map(int, input().split())
for i in Number:
    if i % 2 == 0:
        print(i)

# 1066
Number = map(int, input().split())
for i in Number:
    if i % 2 == 0:
        print("짝")
    else:
        print("홀")
# for i in Number:
#     print("홀" if i % 2 else "짝")

# 1067
N = int(input())
print(N > 0 and "양수" or "음수")
print(N % 2 and "홀수" or "짝수")

print("양수" if N > 0 else "음수")
print("홀수" if N % 2 else "짝수")

# 1068
score = int(input())
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")

# 1069
grade = input()
if grade == "A":
    print("Best")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Run")
elif grade == "D":
    print("Slowly")
else:
    print("?")

# 1070
season = int(input())
if season in [12, 1, 2]:
    print("Winter")
elif season in [3, 4, 5]:
    print("Spring")
elif season in [6, 7, 8]:
    print("Summer")
elif season in [9, 10, 11]:
    print("Fall")
else:
    print("?")

# if 3 <= season < 6:
#     print("Spring")
# elif 6 <= season < 9:
#     print("Summer")
# elif 9 <= season < 12:
#     print("Fall")
# elif 12 < season:
#     print("?")
# else:
#     print("Winter")

