N = int( input() )
A = [0]*(N+2)
for i in range( 1, N+1 ):
    A[i] = int( input() )

left = [0 for _ in range(N+2)]
right = [0 for _ in range(N+2)]
print()
for i in range( 1, N+1 ):
    left[i] = max( left[i-1], A[i] )
    right[N+1-i] = max( right[N+2-i], A[N+1-i] )
left[N+1] = max( A )
right[0] = max( A )

for i in range( 1, N+1 ):
    print( max( left[i-1], right[i+1] ) )