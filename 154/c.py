n = int(input())
A = list(map(int, input().split()))
B = set(A)
print('YES') if len(A)==len(B) else print('NO')