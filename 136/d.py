s = input()
n = len(s)
res = [1 for _ in range(n)]

for i in range(n):
    if s[i] == 'R' and s[i+1] == 'R':
        res[i+2] += res[i]
        res[i] = 0

for i in range(n-1, -1, -1):
    if s[i] == 'L' and s[i-1] == 'L':
        res[i-2] += res[i]
        res[i] = 0

print(*res)