from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

sum_l = [0]+list(accumulate(a))
sum_r = [0]+list(accumulate(a[-1::-1]))

cost = sum_r[-1]
for i in range(n+1):
    cost = min(cost, abs(sum_l[i]-sum_r[n-i]))
print(cost)