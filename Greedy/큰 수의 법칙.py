
# page. 92

N, M, K = map(int, input().split()) # 공백으로 구분하여 세개의 값 받기
N_number = list(map(int, input().split())) # N개의 값을 리스트로 하여 받기
N_number.sort() # 리스트값을 작은값부터 정렬

first = N_number[N - 1] # 가장 큰 수
second = N_number[N - 2] # 두번째 큰 수
sum = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # M의 값이 0이면 탈출
            break
        sum += first
        M -= 1 # 더할 때마다 M값 1씩 빼기
    if M == 0: # M의 값이 0이면 탈출
        break
    sum += second # 두번째 큰 수를 한번 더하기
    M -= 1 # M값 1 빼기

print(sum)

print("---------- 다른풀이 ----------")

n, m, k = map(int, input().split(" ")) # 공백으로 구분하여 세개의 값 받기
n_number = list(map(int, input().split(" "))) # N개의 값을 리스트로 하여 받기
n_number.sort() # 리스트값을 작은값부터 정렬

first = n_number[N - 1] # 가장 큰 수
second = n_number[N - 2] # 두번째 큰 수
count = 0

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)