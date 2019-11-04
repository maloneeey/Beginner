s = input()
k = int(input())
cnt = 1
idx = 0
while idx<len(s)-1:
    if s[idx] == s[idx+1]:
        idx += 2
        cnt += 1
    else:
        idx += 1

cnt *= k
if s[1] == s[-1] and s[-1] != s[-2]:
    cnt += k-1
print(cnt)