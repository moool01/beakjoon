n = int(input())

for i in range(n):
    F,R,P = map(int,input().split())
    Room_num = 0
    while True:
        if P > F:
            P -= F
            Room_num += 1
        else:
            height = P
            break
    print(height*100+Room_num+1)