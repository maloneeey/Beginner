n = int(input())
s = input()

mid = n//2
if n%2 == 0 and s[:mid] == s[mid:]:
    print('Yes')
else:
    print('No')