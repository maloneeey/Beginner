n = int(input())
a = list(map(int, input().split()))

cur, prv = 0, 0
sum_a = sum(a)
mid = sum_a//2
cost = 0
if sum_a%2 != 0:
    cost += 1
    mid += 1
for i in range(n):
    cur += a[i]
    if abs(cur-mid) > abs(prv-mid):
        break
    prv = cur

obj = prv
cost += abs(obj-mid)*2
print(cost)