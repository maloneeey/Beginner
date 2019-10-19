n, k = map(int, input().split())
v = list( map(int, input().split()) )

m = min(n, k)
ans = -10**9
for l in range(m+1):
    for r in range(m-l+1):
        jry = v[:l]+v[-r:] if r>=1 else v[:l]
        t = k - l - r
        s = 0
        for i in sorted(jry):
            if i<0 and t>0:
                s += -i
                t -= 1
        ans = max(ans, sum(jry)+s)

print(ans)