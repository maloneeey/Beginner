n, m = map(int, input().split())
res = ['-1' for _ in range(n)]
for _ in range(m):
    s, c = map(int, input().split())
    if (n > 1 and s == 1 and c == 0) or (res[s-1] != '-1' and res[s-1] != str(c)):
        print(-1)
        exit()
    else:
        res[s-1] = str(c)
for i in range(n):
    if res[i] == '-1':
        res[i] = '1' if i == 0 and n > 1 else '0'
print(''.join(res))