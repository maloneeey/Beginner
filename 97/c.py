s = input()
k = int(input())

subs = set()
for l in range(1, k+1):
    for i in range(len(s)-l+1):
        subs.add(s[i:i+l])
subs = sorted(subs)
print(subs[k-1])