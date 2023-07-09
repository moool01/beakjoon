a = int(input())

for _ in range(a):
    b = input()
    s = list(b)
    score = 0
    c = 0
    for i in s:
        if i == 'O':
            score += 1
            c += score
        else:
            score = 0
    print(c)