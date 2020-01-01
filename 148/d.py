n = int(input())
a = list( map(int, input().split()) )

cnt = 1
ans = 0
flg = False
for i in range(n):
    if cnt == a[i]:
        flg = True
        cnt += 1
    else:
        ans += 1
print(ans) if ans >= 0 and flg else print(-1)