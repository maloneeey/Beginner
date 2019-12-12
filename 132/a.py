s = input()
ltr = []
cnt = []
for a in s:
    if not a in ltr:
        ltr.append(a)
        cnt.append(0)
    else:
        cnt[ltr.index(a)] += 1
print("Yes" if cnt == [1, 1] else "No")
