n = int(input())

def onetwothree(a):
  if a ==1:
    return 1
  if a==2:
    return 2
  if a==3:
    return 4
  else:
    return onetwothree(a-3)+onetwothree(a-2)+onetwothree(a-1)

for i in range(n):
  num = int(input())
  print(onetwothree(num))
