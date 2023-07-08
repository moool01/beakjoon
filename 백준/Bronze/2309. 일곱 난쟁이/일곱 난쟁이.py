height_sum = 0
height_list = []
for i in range(9):
    height = int(input())
    height_sum = height_sum + height
    height_list.append(height)
height_list.sort()
is_ok = False
for first in range(9):
    for second in range(first, 9):
        if first == second:
            continue
        height_total = height_sum - height_list[first] - height_list[second]
        if height_total == 100:
            height_list.remove(height_list[second])
            height_list.remove(height_list[first])
            is_ok = True
            break
    if is_ok:
        break
for height in height_list:
    print(height)