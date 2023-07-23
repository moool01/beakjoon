import sys
from collections import deque

def bfs(v):
    que = deque([v])
    
    while que:
        v = que.popleft()
        if v == k:
            print(arr[v])
            break
        for next in (v-1, v+1, 2*v):
            if 0 <= next < MAX and not arr[next]:
                arr[next] = arr[v] +1
                que.append(next)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
arr = [0] * MAX
bfs(n)
