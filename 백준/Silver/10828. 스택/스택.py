import sys

N =int(input())
list=[]
for _ in range(N):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        list.append(a[1])

    elif a[0] == 'pop':
        if len(list) == 0:
            print(-1)
        else:
            print(list.pop())

    elif a[0] == 'size':
        print(len(list))

    elif a[0] == 'empty':
        if len(list) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'top':
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])