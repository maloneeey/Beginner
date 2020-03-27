s = input()
q = int(input())
a, b = '', ''
cnt = 0
for _ in range(q):
    que = input().split()
    if que[0] == '1':
        cnt += 1
    else:
        if (cnt+int(que[1])) %2 == 0:
            a += que[2]
        else:
            b += que[2]
if cnt%2 == 1:
    s = a[-1::-1]+s[-1::-1]+b
else:
    s = b[-1::-1]+s+a
print(s)