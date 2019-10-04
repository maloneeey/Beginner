import math
n, h, r, t = map(int, input().split())
g = 10.0
y = [ 0 for _ in range(n) ]
s = math.sqrt(2*h/g)

def calc(t):
  if t <= 0:
    return h
  k = int(t/s)
  if k%2==0:
    d = t-k*s
  else:
    d = k*(s+1)-t
  return h-g*d*d/2

for i in range(n):
  y[i] = calc(t-i)
y.sort()
for i in range(n):
  out = y[i]+2*r*i/100
  print("{:.2f}".format( out ))