n = int(input())
A = list(map(int, input().split()))
ans = 0
l, r = 0, 0
s = x = A[l]
flg = True
for l in range(n):
    while s == x and flg:
        r += 1
        if r == n:
            flg = False
            break
        s += A[r]; x ^= A[r]
    ans += r-l
    s -= A[l]
    x ^= A[l]
print(ans)