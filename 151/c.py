n, m = map(int, input().split())
Ps = [ input().split() for _ in range(m)]
Prb = [[-1, -1] for _ in range(n)]
wa, ac = 0, 0
for ps in Ps:
    p, s = int(ps[0])-1, ps[1]
    if Prb[p][0] == -1:
        Prb[p][0] = 0
    if Prb[p][1] == -1:
        if s == 'WA':
            Prb[p][0] += 1
        else:
            Prb[p][1] = 1
            wa += Prb[p][0]
            ac += 1
print(ac, wa)