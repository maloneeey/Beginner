n = int(input())
dirc = input()

dirc_bi = dirc.replace("F", "0").replace("B", "1")
dirc_bi = list( map(int, dirc_bi) )

def calc(k):
  f = [0 for _ in range(n)]
  res = 0
  sum_f = 0
  for i in range(n-k+1):
    if (dirc_bi[i]+sum_f)%2 != 0:
      res += 1
      f[i] = 1
    sum_f += f[i]
    if i-k+1 >= 0:
      sum_f -= f[i-k+1]

  for i in range(n-k+1, n):
    if (dirc_bi[i]+sum_f)%2 != 0:
      return -1
    if i-k+1 >= 0:
      sum_f -= f[i-k+1]

  return res

K, M = 1, n
for k in range(1, n+1):
  m = calc(k)
  if m>=0 and M>m:
    M, K = m, k

print("K={}, M={}".format(K,M))
