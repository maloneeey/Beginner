from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
a = list(map(int, input().split()))

SIZE = 10**3
bucket = []
for i in range(int(n/SIZE)):
    bucket.append(sorted(a[SIZE*i:SIZE*(i+1)]))
nums = sorted(a.copy())

for _ in range(m):
    i, j, k = map(int, input().split())
    l, r = i, j+1

    lb = -1; ub = n-1
    while ub-lb > 1:
        md = int( (lb+ub)/2 )
        x = nums[md]
        tl, tr, c = l, r, 0

        while tl<tr and tl%SIZE != 0:
            if a[tl] <= x:
                c += 1
            tl += 1

        while tl<tr and tr%SIZE != 0:
            if a[tr] <= x:
                c += 1
            tr += 1

        while tl<tr:
            b = int(tl/SIZE)
            c += bisect_right(bucket[b], x)
            tl += SIZE

        if c>=k:
            ub = md
        else:
            lb = md
print(nums[ub])
