n = int(input())
s = input()
i = 0
ans = 0
while i<n:
    if 'ABC' in s[i:min(i+3, n)]:
        ans += 1
        i += 3
    else:
        i += 1
print(ans)