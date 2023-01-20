n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
if k > 1:
    if k == n:
        print(nums[-1])
    elif nums[k] == nums[k-1]:
        print(-1)
    else:
        print((nums[k]+nums[k-1])//2)
elif k == 1:
    if nums.count(nums[0]) == 1:
        print(nums[0])
    else:
        print(-1)
else:
    if nums[0] > 1:
        print(nums[0]-1)
    else:
        print(-1)
