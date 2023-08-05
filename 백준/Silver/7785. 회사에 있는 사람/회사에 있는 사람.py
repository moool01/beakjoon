import sys
n = int(sys.stdin.readline())
temp = dict() # 딕셔너리 형

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    if b == "enter":
        temp[a] = b
    # 퇴근을 했으면 삭제해준다.
    elif b == "leave":
        del temp[a]

# 사전 순의 역순으로 정렬한다.
temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)
