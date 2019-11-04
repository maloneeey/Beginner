k, x = map(int, input().split())
edge = 10**6
left = max( x-k+1, -edge )
right = min( x+k-1, edge )
res = [ i for i in range(left, right+1) ]
print(*res)