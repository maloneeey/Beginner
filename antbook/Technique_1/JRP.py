p = int(input())
a = list( map(int, input().split()) )

b = set(a)
s, t = 0, 0
res = p
while t<p:
  if set(a[s:t+1])==b:
    res = min(res, t-s+1)
    s += 1
  else:
    t += 1

print(res)