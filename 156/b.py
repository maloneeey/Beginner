n, k = map(int, input().split())
cnt = 0
while n >= k**cnt:
    cnt += 1
print(cnt)