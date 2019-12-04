import sys
input = sys.stdin.readline

def idx(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

n = int(input())
s = list(input())

cnt = 0
for abc in range(1000):
    abc = list(str(abc).zfill(3))
    i = 0
    for dig in s:
        if dig == abc[i]:
            i += 1
            if i == 3:
                break
    if i == 3:
        cnt += 1

print(cnt)