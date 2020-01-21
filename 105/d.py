import sys
from itertools import accumulate
n, m = map(int, input().split())
A = list(map(int, input().split()))
A = [0]+list(accumulate(A))

for i in range(n+1):
    A[i] %= m
A.sort()
ans = 0; cnt = 1
for i in range(n):
    if A[i] == A[i+1]:
        cnt += 1
        if i == n-1:
            ans += cnt*(cnt-1)//2
    else:
        ans += cnt*(cnt-1)//2
        cnt = 1

print(ans)