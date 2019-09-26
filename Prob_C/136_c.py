N = int( input() )
H = list( map( int, input().split() ) )

for i in range( N-1, 0, -1 ):
    if H[i-1] > H[i]:
        H[i-1] = H[i-1] - 1

tmp = 0
for i in range( N-1 ):
    if H[i] > H[i+1]:
        tmp = 1
        break

if tmp == 0:
    print('Yes')
else:
    print('No')