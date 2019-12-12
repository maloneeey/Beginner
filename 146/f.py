import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input().strip()

ans = []

now = n
while now != 0:
    tmp = False
    for i in range(m, 0, -1):
        if now-i >= 0 and s[now-i] == '0':
            tmp = True
            now -= i
            ans.append(i)
            break
    if not tmp:
        print(-1)
        sys.exit()
print(*ans[::-1])