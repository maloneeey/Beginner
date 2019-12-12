n = int(input())
a = list(map(int, input().split()))

zero = 0
minus = 0
for i in range(n):
    if a[i] == 0:
        zero = 1
    elif a[i] < 0:
        minus += 1
    a[i] = abs(a[i])

a.sort()
if zero or minus%2 == 0:
    print(sum(a))
else:
    print(sum(a[1:])-a[0])