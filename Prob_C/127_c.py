n, m = map(int, input().split())
l, r = [], []
for _ in range(m):
  l_, r_ = map(int, input().split())
  l.append(l_)
  r.append(r_)

res = min(r)-max(l)+1
output = res if res > 0 else 0
print(output)