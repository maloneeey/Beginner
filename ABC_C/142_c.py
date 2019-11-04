n = int(input())
a = list(map(int, input().split()))
arv = [ 0 for _ in range(n) ]

for i in range(n):
    arv[a[i]-1] = i+1

for i in range(n):
    print(arv[i], end=" ")
