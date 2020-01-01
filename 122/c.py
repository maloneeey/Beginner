n, q = map(int, input().split())
s = input()

flg = False
acm = []
cnt = 0
for a in s:
    if a == 'A':
        flg = True
    elif a == 'C' and flg:
        cnt += 1

    if a != 'A':
        flg = False
    acm.append(cnt)

for _ in range(q):
    l, r = map(int, input().split())
    print(acm[r-1]-acm[l-1])