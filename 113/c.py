n, m = map(int, input().split())
Py = []
for i in range(m):
    py = list(map(int, input().split()))
    Py.append(py+[i])
Py = sorted(sorted(Py, key = lambda x: x[1]))
tmp = -1
ans = []
for i in range(m):
    out = str(Py[i][0]).zfill(6)
    cnt = cnt + 1 if Py[i][0] == tmp else 1
    out += str(cnt).zfill(6)
    tmp = Py[i][0]
    ans.append([Py[i][2], out])
ans.sort()
for i in range(m):
    print(ans[i][1])