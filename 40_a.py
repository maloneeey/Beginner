import sys

input = sys.stdin.readline
s = input()
lft, rgt = 0, 0
cnt = 0
tmp = ""
for cur in s:
    if tmp == ">" and cur == "<":
        lar = max(lft, rgt)+1
        sma = min(lft, rgt)
        cnt += sum(range(lar)) + sum(range(sma))
        lft, rgt = 1, 0
    elif cur == ">":
        rgt += 1
    elif cur == "<":
        lft += 1
    tmp = cur

lar = max(lft, rgt)+1
sma = min(lft, rgt)
cnt += sum(range(lar)) + sum(range(sma))
print(cnt)
