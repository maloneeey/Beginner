n = int(input())
dct = {}
for _ in range(n):
    s = input()
    if s in dct:
        dct[s] += 1
    else:
        dct[s] = 1
m = max(dct.values())
ans = []
for a, v in dct.items():
    if v == m:
        ans.append(a)
ans.sort()
for a in ans:
    print(a)