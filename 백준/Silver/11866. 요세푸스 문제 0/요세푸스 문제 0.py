from collections import deque

result = []
n, k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<",end='')
for i in range(len(result)-1):
    print("%d, " %result[i], end='')
print(result[-1], end='')
print(">")