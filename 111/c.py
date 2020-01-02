from collections import Counter
n = int(input())
V = list(map(int, input().split()))

Odd, Evn = [], []
for i in range(n):
    Evn.append(V[i]) if i%2 == 0 else Odd.append(V[i])
Evn = sorted( dict(Counter(Evn)).items(), key = lambda x:x[1], reverse=True)
Odd = sorted( dict(Counter(Odd)).items(), key = lambda x:x[1], reverse=True)

cnt = -1
for evn in Evn[0:2]:
    for odd in Odd[0:2]:
        if evn[0] != odd[0]:
            cnt = max(cnt, evn[1]+odd[1])
print(n-cnt) if cnt > 0 else print(n//2)