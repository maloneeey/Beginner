n = int(input())
v1 = list( map(int, input().split()) )
v2 = list( map(int, input().split()) )

v1.sort()
v2.sort(reverse=True)
innerProduct = 0
for i in range(n):
    innerProduct += v1[i]*v2[i]
print(innerProduct)