# 1 분에 한 대당 A원, 1분에 두 대당 B원, 1분에 세 대당 C원
A,B,C = map(int, input().split())

# 입력으로 주어지는 시간 1~100 사이 --> 100개 요소가 들어가는 0 리스트 생성
hours = [0 for _ in range(100)]

# 도착과 출발 시간에 해당되는 자릿수에 1을 추가해주기  (동시간에 차 대수 구하기)
for _ in range(3):
    arrive,depart = map(int,input().split())

    for i in range(arrive, depart):
        hours[i] += 1


# 계산하기
total_price = hours.count(1) * A + hours.count(2) * B * 2 + hours.count(3) * C *3

print(total_price)