import sys

N =int(input())
stack=[]
for _ in range(N):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        stack.append(a[1])

    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif a[0] == 'size':
        print(len(stack))

    elif a[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
