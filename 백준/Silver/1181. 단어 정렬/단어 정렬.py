n = int(input())

word = []
for i in range(n):
    word.append(input())

word = list(set(word))
word.sort()
word.sort(key = len)
final = word
# print(type(final))
for i in range(len(final)):
    print(final[i])
# print(result)