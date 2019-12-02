import sys
input = sys.stdin.readline

H, W, K = map(int, input().split())
ans = []
vac = []
num = 1
flg = 0
for i in range(H):
    cnt = 0
    res = []
    a = input()
    if '#' in a:
        for b in a[:-1]:
            if b == '#':
                cnt += 1
                if cnt > 1:
                    num += 1
            res.append(num)
        ans.append(res)
        num += 1
    else:
        if i == 0:
            flg = 1
            continue
        else:
            vac.append(i)

if flg:
    ans.insert(0, ans[0])
for k in vac:
    ans.insert(k, ans[k-1])

for a in ans:
    print(*a)
