n = int(input())
s = input()

res = 0
i,j = 0, 1
while j<n:
    if s[i:j] in s[j:]:
        res = max(res, j-i)
        j += 1
    else:
        i += 1
    if i==j:
        i += 1
        j += 2
print(res)