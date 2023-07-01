A, B = map(int, input().split()) # 시 분 순서로 입력
C = int(input()) # 추가하는부분 분 추가

hour = A + (B+C)//60
min = (B+C)%60

if hour >= 24:
    hour = hour-24

print(hour, min)
