n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 1
tmp = a[0]; cnt = 0
while True:
    if r >= n and tmp < k:
        break

    if tmp >= k:
        cnt += n-r+1
        tmp -= a[l]
        l += 1
    else:
        tmp += a[r]
        r += 1

print(cnt)