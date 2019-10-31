import sys
input = sys.stdin.readline

N = int(input())
A = list( map(int, input().split()) )
x = [0]*N
SUM = sum(A)
x[0] = SUM
for i in range(1, N, 2):
    x[0] -= 2*A[i]
for i in range(1, N):
    x[i] = 2*A[i-1]-x[i-1]
print(*x)