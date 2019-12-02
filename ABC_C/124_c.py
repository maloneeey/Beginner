S = list(input())

tmp = S[0]
cnt = 0
for i in range(1, len(S)):
    if S[i] == tmp:
        cnt += 1
        if S[i] == '0':
            S[i] = '1'
        else:
            S[i] = '0'
    tmp = S[i]
print(cnt)