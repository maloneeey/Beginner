p,q = map(int, input().split())
A = list( map(int, input().split()) )

dp = [ [ 0 for _ in range(q+2)] for _ in range(q+1) ]
A.insert(0, 0)
A.isnert(q+1, p+1)