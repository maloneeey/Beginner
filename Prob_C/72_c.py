n = int(input())
a = list(map(int, input().split()))
ary = [0 for _ in range(10**5)]

for i in range(n):
    if a[i] > 1:
        ary[a[i]-2] += 1
        ary[a[i]-1] += 1
    ary[a[i]] += 1

print(max(ary))