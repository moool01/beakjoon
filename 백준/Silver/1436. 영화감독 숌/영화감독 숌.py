N = int(input())
num = 0
cnt = 0
for i in range(1000000000000000):
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        num = i
        break
print(num)