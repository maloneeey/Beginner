S = input()
T = input()
d0, d1 = {}, {}
for s, t in zip(S, T):
    if s in d0:
        if d0[s] != t:
            print('No')
            exit()
    elif t in d1:
        if d1[t] != s:
            print('No')
            exit()
    else:
        d0[s] = t; d1[t] = s
print('Yes')