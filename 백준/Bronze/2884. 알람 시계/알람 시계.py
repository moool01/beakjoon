import sys
H, M = map(int, sys.stdin.readline().split())
if M > 44:
    print(H,M-45)
else:
    if H == 0:
        print(23,M+15)
    else:
        print(H-1,M+15)