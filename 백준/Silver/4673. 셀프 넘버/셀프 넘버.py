numbers = set(range(1, 10001))  #1~10000까지의 숫자 set
constructed_num = set()  #빈 set(생성자가 있는 숫자 set)

for i in numbers:  #86
    for j in str(i):  #j = 8, 6
        i += int(j) #i = 86 + 8 + 6 = 100
    constructed_num.add(i)  #생성자가 있는 숫자 추가

self_numbers = sorted(numbers - constructed_num)

for num in self_numbers:
  print(num)