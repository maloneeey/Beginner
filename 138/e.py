from bisect import bisect_right
s = input()
t = input()
d = {}

for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += [i]
    else:
        d[s[i]] = [i]

count = 0
cur = -1
for i in t:
    if i not in d:
        print(-1)
        exit()
    if cur < d[i][-1]:
        cur = d[i][bisect_right(d[i], cur)]
        continue
    else:
        count += 1
        cur = d[i][0]
print(count*len(s)+cur+1)