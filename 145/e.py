import sys
input = sys.stdin.readline

n, t = map(int, input().split())
food_l = []
for _ in range(n):
    a, b = map(int, input().split())
    food_l.append((a, b))
food_r = food_l[::-1]

dp_l = [ [0]*t for _ in range(n+1) ]
dp_r = [ [0]*t for _ in range(n+1) ]
for i in range(1, n+1):
    a_l, b_l = food_l[i-1]
    a_r, b_r = food_r[i-1]
    for j in range(t):
        dp_l[i][j] = max(dp_l[i][j], dp_l[i-1][j])
        if j + a_l < t:
            dp_l[i][j+a_l] = max(dp_l[i][j+a_l], dp_l[i-1][j]+b_l)
        
        dp_r[i][j] = max(dp_r[i][j], dp_r[i-1][j])
        if j + a_r < t:
            dp_r[i][j+a_r] = max(dp_r[i][j+a_r], dp_r[i-1][j]+b_r)

ans = 0
for i in range(n):
    res = max(food_l[i][1]+dp_l[i][j]+dp_r[n-i-1][t-j-1] for j in range(t))
    ans = max(res, ans)
print(ans)