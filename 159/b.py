s = input()
t = s[:len(s)//2]
u = s[len(s)//2+1:]
print('Yes') if s == s[::-1] and t == t[::-1] and u == u[::-1] else print('No')