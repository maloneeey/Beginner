s = list(input())
s_rev = list(reversed(s))

count = 0
for i in range(len(s)):
    if s[i] != s_rev[i]:
        count += 1
print(int(count/2))