s = list(input())
left = int( s[0]+s[1] )
right = int( s[2]+s[3] )

if 1 <= left <= 12:
    if 1 <= right <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 1 <= right <= 12:
        print('YYMM')
    else:
        print('NA')