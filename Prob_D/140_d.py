N, K = map(int, input().split())
s = list(input())
if s[0] == 'L':
    s.insert(0, 'R')
else:
    s.insert(0, 'L')

if s[N] == 'L':
    s.append('R')
else:
    s.append('L')

for _ in range(K):
    t = s.copy()
    for i in range(0, N+1):
        if s[i] != s[i+1]:
            start = i+1
    for i in range(N+1, 0, -1):
        if s[i] != s[i-1]:
            end = i-1
    if end <= start:
        break
    for i in range(end-start+1):
        if t[start+i] == 'L':
            s[end-i] = 'R'
        else:
            s[end-i] = 'L'
    if s[1] == 'L':
        s[0] = 'R'
    else:
        s[0] = 'L'
    if s[N] == 'L':
        s[N+1] = 'R'
    else:
        s[N+1] = 'L'

count = 0
for i in range(1, N):
    if s[i] == s[i+1]:
        count = count + 1

print(count)