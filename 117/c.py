n, m = map(int, input().split())
X = list( map(int, input().split()) )

X.sort()
Xx = sorted( [ X[i+1]-X[i] for i in range(m-1) ], reverse=True )
print(sum(Xx[n-1:]))