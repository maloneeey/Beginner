n = int(input())
s_1 = input()
s_2 = input()

i = 0
cnt = []

if n>1:
    isCnt = ( s_1[0] == s_1[1] )
    cnt.append(isCnt)
if n>2:
    for i in range(1, n-1):
        isCnt = ( s_1[i-1]==s_1[i] or s_1[i]==s_1[i+1] )
        cnt.append(isCnt)
if n>3:
    isCnt = ( s_1[n-2] == s_1[n-1] )
    cnt.append(isCnt)

count = 3
for i in range(1, n):
    if cnt[i-1]:
        if i==1:
            count = count * 2
    elif cnt[i]:
        count = count * 2
    else:
        count = count * 2
print(count)
