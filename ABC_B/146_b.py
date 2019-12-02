n = int(input())
s = input()

def rot(c, n):
    return chr(( ord(c)-ord('A') + n) % 26 + ord('A'))

for a in s:
    print(rot(a, n), end='')