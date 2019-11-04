n, m = map(int, input().split())
s = []
for _ in range(m):
    s_ = list(map(int, input().split()))
    s.append(s_)
p = list(map(int, input().split()))

cnt = 0
for i in range(pow(2, n)):
    switch = [i>>j&1 for j in range(n)]
    light = 0
    for j in range(m):
        on = 0
        for k in s[j][1:]:
            if switch[k-1]==1:
                on += 1
        if on%2 == p[j]:
            light += 1
    if light == m:
        cnt += 1
print(cnt)