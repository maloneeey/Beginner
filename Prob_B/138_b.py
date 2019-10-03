n = int(input())
a = list( map(int, input().split()) )

dnm = 1/a[0]
for i in range(1, n):
  dnm += 1/a[i]
print(1/dnm)