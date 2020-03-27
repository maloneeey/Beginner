n, a, b = map(int, input().split())
l = n % (a+b)
m = n // (a+b)
res = a*m + l if l < a else a*m+a
print(res)