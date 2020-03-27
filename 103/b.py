s = input()
t = input()

for _ in range(len(s)):
    if s == t:
        print('Yes')
        exit()
    t = t[-1] + t[:-1]
print('No')