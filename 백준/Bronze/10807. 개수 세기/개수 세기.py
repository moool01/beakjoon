N = int(input())
line = list(map(int,input().split()))
v = int(input())
# print(N,X)

# print(type(line))

count =0
for i in range(N):
    if v == line[i]:
        count += 1

print(count)