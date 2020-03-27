n = int(input())
A = list(map(int, input().split()))

nums = {}
for a in A:
    nums[a] = nums[a] + 1 if a in nums else 1
res = 0
for key in nums.keys():
    res += nums[key]*(nums[key]-1)//2
for a in A:
    print( res-nums[a]+1 )