s = input()
acgt = 'ACGT'
res = 0
cnt = 0

for a in s:
    cnt += 1
    if not a in acgt:
        cnt = 0
    res = max(res, cnt)
print(res)