n, k = map(int, input().split())
w, v = [], []
for _ in range(n):
  w_, v_ = map(int, input().split())
  w.append(w_)
  v.append(v_)

def C(x):
  y = []
  for i in range(n):
    y.append( v[i]-x*w[i] )
  y.sort(reverse=True)
  ySum = 0
  for i in range(k):
    ySum += y[i]

  return ySum >= 0

lb, ub = 0, max(v)
for i in range(100):
  mid = (lb+ub)/2
  if C(mid):
    lb = mid
  else:
    ub = mid

print( "{}".format( int(ub*100)/100 ) )