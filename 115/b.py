n = int(input())
P = []
for _ in range(n):
    P.append(int(input()))
P.sort(reverse=True)
print(int(P[0]/2)+sum(P[1:]))