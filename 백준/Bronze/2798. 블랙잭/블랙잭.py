a,b = map(int,input().split())
card_list = list(map(int,input().split()))
list=[]
card_list.sort()
is_ok = False
for first in range(a):
    for second in range(first+1, a):
        for third in range(second+1,a):
            card_sum = card_list[first] + card_list[second] + card_list[third]
            if card_sum > b:
                continue
            else:
                list.append(card_sum)
print(max(list))