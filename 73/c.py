n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

cnt = 1; ans = 0
for i in range(1, n):
    if a[i] == a[i-1]:
        cnt ^= 1
    else:
        ans += cnt
        cnt = 1
ans += cnt
print(ans)