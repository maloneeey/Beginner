n, k, m = map(int, input().split())
A = list(map(int, input().split()))
print(max(0, n*m-sum(A))) if n*m-sum(A) <= k else print('-1')