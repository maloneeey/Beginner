n, q = map(int, input().split())
a = list( map(int, input().split()) )

DAT_SIZE = 1<<18 - 1
whole = [0*DAT_SIZE]
part = [0*DAT_SIZE]

def sg_add(a, b, x, k, l, r):
    if a<=l and r<=b:
        whole[k] += x
    elif l<b and a<r:
        part[k] += (min(b,r)-max(a,l))*x
        sg_add(a, b, x, k*2+1, 1, (l+r)/2)
        sg_add(a, b, x, k*2+2, (l+r)/2, r)

def sg_sum(a, b, k, l, r):
    if b<=l or r<=a:
        return 0
    elif a<=l and r<=b:
        return whole[k]*(r-l) + part[k]
    else:
        res = (min(b, r)-max(a, l))*whole[k]
        res += sg_sum(a, b, k*2+1, l, (l+r)/2)
        res += sg_sum(a, b, k*2+2, (l+r)/2, r)
        return res

for i in range(n):
    sg_add(i, i+1, a[i], 0, 0, n)

for _ in range(n):
    t = input()
    if t == 'C':
        l, r, x = map(int, input().split())
        sg_add(l, r+1, x, 0, 0, n)
    else:
        print(sg_sum(l, r+1, 0, 0, n))