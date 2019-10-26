from bisect import bisect_right, bisect_left
n = int(input())
l = list(map(int, input().split()))
count = 0
l.sort()
for i in range(n-2):
    for j in range(i+1, n-1):
        count += bisect_left(l, l[i]+l[j]) -j -1
print(count)