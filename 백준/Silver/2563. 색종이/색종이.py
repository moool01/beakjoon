N = int(input())
total = 0
A = [[0 for _ in range(101)]for _ in range(101)]

for i in range(N):
    a,b= map(int,input().split())
    for k in range(a,a+10):
        for m in range(b, b+10):
            A[k][m] = 1

r = 0
for i in A:
    r += sum(i)
print(r)