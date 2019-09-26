N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )
fii = [0]*N
fij = [0]*N

fii[0] = min( A[0], B[0] )
for i in range( 0, N-1 ):
    fij[i] = min( A[i+1], B[i]-fii[i] )
    fii[i+1] = min( A[i+1]-fij[i], B[i+1] )
fij[N-1] = min( B[N-1]-fii[N-1], A[N] )

count = 0
for i in range( 0, N ):
    count = count + fii[i] + fij[i]

print(count)