n = int(input())
a = [-1]+list( map(int, input().split()) )
b = [0]*(n+1)
res = 0
ary = []

for i in range(n, 0, -1):
    tmp = 0
    for j in range( 2*i, n+1, i ):
        tmp += b[j]
    if tmp%2 != a[i]:
        res += 1
        b[i] = 1
for i in range(1, n+1):
    if b[i] == 1:
        ary.append(i)
print(res)
if res != 0:
    print(*ary)