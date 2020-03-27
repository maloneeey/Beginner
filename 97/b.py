x = int(input())
res = 1
for b in range(2, int(pow(x, 1/2))+1):
    for p in range(2, x):
        if b**p <= x:
            res = max(res, b**p)
        else:
            break
print(res)