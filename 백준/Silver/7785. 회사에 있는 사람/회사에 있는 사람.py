import sys
n = int(sys.stdin.readline())
temp ={}

for _ in range(n):
  a,b = map(str,sys.stdin.readline().split())

  if b == "enter":
    temp[a] = b
  elif b == "leave":
    del temp[a]

temp = sorted(temp.keys(),reverse=True)

for i in temp:
  print(i)
