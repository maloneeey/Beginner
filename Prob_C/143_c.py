n = int(input())
s = list(input())
count = 1
for i in range(1, n):
    if s[i-1] == s[i]:
        continue
    else:
        count += 1

print(count)