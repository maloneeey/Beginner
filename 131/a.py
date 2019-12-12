s = input()

flg = 0
for i in range(3):
    if s[i] == s[i+1]:
        flg = 1
print( 'Bad' if flg else 'Good' )