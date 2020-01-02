n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))

ans = -1
dif = 10**6
for i in range(n):
    if abs(t-0.006*H[i]-a) < dif:
        dif = abs(t-0.006*H[i]-a)
        ans = i+1
print(ans)