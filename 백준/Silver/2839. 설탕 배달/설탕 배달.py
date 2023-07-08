a = int(input())
cnt = 0
while a >= 0:
    if a % 5 == 0:
        print(a//5+cnt)
        break
    a -= 3
    cnt += 1

else:
    print(-1)