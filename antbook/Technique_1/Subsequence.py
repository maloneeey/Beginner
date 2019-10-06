from itertools import accumulate
from bisect import bisect_left
n, s = map(int, input().split())
a = list(map(int, input().split()))
acm = list( accumulate(a) )

if acm[-1] < s:
    print(0)
else:
    res = n
    i = 0
    while acm[i]+s <= acm[-1]:
        t = bisect_left(acm, acm[i]+s)
        res = min(res, t-i)
        i += 1

print(res)
