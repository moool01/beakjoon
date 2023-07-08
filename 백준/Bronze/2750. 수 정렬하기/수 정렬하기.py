N = int(input())
nums = [0 for _ in range(N)]

for i in range(N):
    nums[i]=int(input())

for i in range(N):
    idx = i
    for j in range(i+1,N):
        if nums[idx] > nums[j]:
            idx = j

    nums[i] ,nums[idx] = nums[idx] , nums[i]

for i in nums:
    print(i)