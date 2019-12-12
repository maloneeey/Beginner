a, b, x = map(int, input().split())

l = 0
r = 10**9

while r-l>1:
    mid = (l+r)//2
    d = len(str(mid))
    if a*mid+b*d<=x:
        l = mid
    else:
        r = mid

d = len(str(l+1))
if a*(l+1)+b*d<=x:
    l += 1
print(l)