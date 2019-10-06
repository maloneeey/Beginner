from itertools import combinations_with_replacement
n, m = map(int, input().split())
s = []
for _ in range(m):
  s_ = list(map(int, input().split()))
  s.append(s_)
p = list(map(int, input().split()))

onoff = [0, 1]
cnt = 0
for switch in combinations_with_replacement(onoff, n):
  for i in range(m):
    on = 0
    for j in range(1, s[i][0]+1):
      if switch[ s[i][j]-1 ] == 1:
        on += 1
    if on%2 == p[i]:
      cnt += 1
print(cnt)
