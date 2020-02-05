n, k = map(int, input().split())
H = sorted(list(map(int, input().split())), reverse=True)
print(sum(H[k:]))