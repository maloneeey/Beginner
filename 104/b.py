s = input()
def cntUpper(s):
    cnt = 0
    for a in s:
        if a.isupper():
            cnt += 1
    return cnt
print('AC') if s[0] == 'A' and 'C' in s[2:-1] and cntUpper(s) == 2 else print('WA')