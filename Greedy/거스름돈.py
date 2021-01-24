
# page. 87
# 당신은 음식점의 계산을 도와주는 점원이다.
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
# 손님에세 거슬러 줘야 할 돈이 N눰일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

coin_count = 0
charge =int(input("거스름돈을 입력하시오.\n"))

coin_type = [500, 100, 50, 10]
for coin in coin_type:
    coin_count += charge // coin
    charge %= coin

print(coin_count)