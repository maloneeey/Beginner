N = int(input())
p = list(map(int, input().split()))

secondSum = 0
for i in range(N):
    pmax = p[i]
    for j in range(i+1, N):
        first = max(pmax, p[j])
        second = min(pmax, p[j])
        secondSum = secondSum + second
        pmax = max(pmax, p[j])

print(secondSum)