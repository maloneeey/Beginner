n = int(input())
P, A = [2], [2]
for i in range(3, 55556, 2):
    for p in P:
        if i % p == 0: break
    else:
        P.append(i)
        if i % 5 == 2: A.append(i)
    if len(A) == n: break
print(*A)