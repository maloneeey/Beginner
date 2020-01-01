n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

def rsp(x):
    if x=='r':
        return 'p'
    elif x=='s':
        return 'r'
    else:
        return 's'

Ban = ['']*k+[ rsp(t[i]) for i in range(n-k) ]
res = 0
for i in range(n):
    if rsp(t[i]) != Ban[i]:
        if rsp(t[i]) == 'r':
            res += r
        elif rsp(t[i]) == 's':
            res += s
        else:
            res += p
    elif i+k<n:
        Ban[i+k] = ''
print(res)