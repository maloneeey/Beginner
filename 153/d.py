h = int(input())
ans = 0; cnt = 1
while h >= 1:
    ans += cnt
    h //= 2
    cnt *= 2
print(ans)