num = []
for i in range(10):
    a = int(input())
    num.append(a%42)
nums = set(num)
print(len(nums))