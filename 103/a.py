A = list(map(int, input().split()))
A.sort(reverse=True)
print(sum( [ abs(A[i+1]-A[i]) for i in range(2) ] ))