N, K = map(int, input().split())
S = input()

l = 0
alt = 0; cnt = 0

for r in range(N):
    if S[r] == '0' and ( r == 0 or S[r-1] == '1'):
        alt += 1
    if alt > K:
        while S[l] == '1':
            l += 1
        while S[l] == '0':
            l += 1
        alt -= 1
    cnt = max(cnt, r-l+1)
print(cnt)