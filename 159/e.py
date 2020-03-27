h, w, k = map(int, input().split())
S = [ [ int(i) for i in input()] for _ in range(h) ]
res = 10**4
for i in range( 1<<(h-1) ):
    pos = [0]*h
    x = 0
    for j in range(h-1):
        if i & ( 1 << j ):
            x += 1
        pos[j+1] = x

    ret = x
    x = 0
    cnt = [0]*h
    flag = 0
    while x < w:
        for y in range(h):
            cnt[pos[y]] += S[y][x]
            if cnt[pos[y]] > k:
                cnt = [0]*h
                ret += 1
                flag += 1
                break
        else:
            x += 1
            flag = 0

        if flag == 2:
            ret = 10**4
            break

    res = min(res, ret)
print(res)