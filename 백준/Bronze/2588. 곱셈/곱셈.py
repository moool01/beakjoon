first =int(input())
second =input()

fifth= int(second[0]) * first # 백의 자리수 계산
fourth= int(second[1]) * first #십의 자리수 계산
third = int(second[2]) * first #일의 자리수 계산
result= first * int(second)

print(third)
print(fourth)
print(fifth)
print(result)