n = int( input() )
s = input()
t = ''

a = 0
b = n-1
while a <= b:
    left = False
    i = 0
    while a + i <= b:
        if s[a+i] < s[b-i]:
            left = True
            break
        elif s[a+i] > s[b-i]:
            left = False
            break
        i = i + 1

    if left:
        t = t + s[a]
        a = a + 1
    else:
        t = t + s[b]
        b = b - 1

print(t)