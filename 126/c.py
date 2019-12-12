n, k = map(int, input().split())

prob = 0
for i in range(1, n+1):
    j = 0
    tmp = 1/n
    while i*pow(2, j) < k:
        tmp /= 2
        j += 1
    prob += tmp
print(prob)