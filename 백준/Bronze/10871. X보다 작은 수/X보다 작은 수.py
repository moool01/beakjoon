N, X = map(int,input().split())
line = list(map(int,input().split()))

# print(N,X)

# print(type(line))


for value in line:
    if value <X:
        print(value, end = ' ')