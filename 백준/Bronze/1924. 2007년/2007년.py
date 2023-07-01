import sys

day = 0
month = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
a, b = map(int, sys.stdin.readline().split())

for i in range(a-1):
    day += month[i]

day = day + b

weekno = day%7

print(week[weekno])