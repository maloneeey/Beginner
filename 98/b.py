n = int(input())
s = input()
res = 0
for i in range(1, n-1):
    s1 = set(s[:i])
    s2 = set(s[i:])
    res = max(res, len(s1&s2))
print(res)