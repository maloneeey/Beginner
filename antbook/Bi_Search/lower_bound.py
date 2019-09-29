n = int( input() )
a = list( map(int, input().split()) )
k = int( input() )

lb, ub = -1, n
while ub-lb > 1:
    mid = int( (lb+ub)/2 )
    if a[mid] >= k:
        ub = mid
    else:
        lb = mid
print(ub)