
list = list(map(int, input().split()))
for i in range(len(list)):
    list[i] = ((list[i]**2)%10)

print(sum(list)%10)

