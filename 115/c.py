n, k = map(int, input().split())
H = []
for _ in range(n):
    H.append(int(input()))
H.sort()
Dif = [ H[i+k-1]-H[i] for i in range(n-k+1)]
print(min(Dif))