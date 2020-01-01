n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
cnt = 0
ans = 0
i = 0
while cnt<2*m:
    cnt += 2*(m-1-i)
    ans += 2*(m-1-i)*A[i]
    if cnt>2*m:
        ans -= (cnt-2*m)*A[i]
print(ans)