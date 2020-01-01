N = int(input())
A = list(map(int, input().split()))

while True:
    MOD = min(A)
    for i in range(N):
        A[i] = A[i]%MOD if A[i]%MOD != 0 else A[i]
    if MOD == min(A):
        break
print(MOD)