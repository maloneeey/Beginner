import sys
MOD = 10**9+7

n = int(input())
A = list(map(int, input().split()))
prmMax = int(pow(max(A), 0.5))+1
Prm = [ [0]*prmMax for _ in range(n) ]

def keepAsPrime(x, List):
    for i in range(1, int(pow(x, 1/2))+2):
        if x%i == 0:
            List[i] += 1

for i in range(n):
    keepAsPrime(A[i], Prm[i])
print(Prm)
Lcm = [ max(Prm[:][i]) for i in range(1, prmMax+1) ]
print(Lcm)
ans = 0
for a in A:
    ans = (ans+lcm//a)%MOD
print(ans)