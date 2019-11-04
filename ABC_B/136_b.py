cnt = 0
n = int(input())
if n>=10:
    cnt += 9
    if n>=1000:
        cnt += 900
        if n>=100000:
            cnt += 90000
        elif n>=10000:
            cnt += n-9999
    elif n>=100:
        cnt += n-99
else:
    cnt += n
print(cnt)