import sys
N = int(sys.stdin.readline())

list = []
for i in range(N):
    a = int(sys.stdin.readline())
    list.append(a)
list.sort()
for i in range(N):
    print(list[i])