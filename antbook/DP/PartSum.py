def dfs( i, sum ):
    if i == n:
        return sum == k

    if dfs( i+1, sum) :
        return True

    if dfs( i+1, sum+a[i] ):
        return True

    return False

n, k = map(int, input().split())
a = list( map( int, input().split() ) )

if dfs( 0, 0 ):
    print("Yes")
else:
    print("No")