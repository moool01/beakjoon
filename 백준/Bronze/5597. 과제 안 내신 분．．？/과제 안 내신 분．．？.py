lst = []
loser =[]
for i in range(28):
    lst.append(int(input()))

for i in range(1,31):
    if i not in lst:
        loser.append(i)
        continue
# print(lst)
# print(loser)

for i in range(2):
    print(loser[i])