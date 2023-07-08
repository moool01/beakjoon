N,M = map(int,input().split())
list = [0 for _ in range(N)]

for n in range(N):
    list[n] = n+1

for _ in range(1,M+1):
    i , j = map(int, input().split())
    list[i-1], list[j-1] = list[j-1], list[i-1]

for n in range(N):
    print(list[n], end = ' ')