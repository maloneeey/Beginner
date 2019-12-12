from itertools import accumulate
n = int(input())
w = list(map(int, input().split()))

acm = [0]+list(accumulate(w))
acm_rev = [0]+list(accumulate(reversed(w)))
acm_rev.reverse()

wgt = 100
for i in range(n+1):
    wgt = min(wgt, abs(acm[i]-acm_rev[i]))
print(wgt)