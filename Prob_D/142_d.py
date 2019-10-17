from fractions import gcd
a, b = map(int, input().split())
n = gcd(a, b)

divisors = []
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        divisors.append(i)
        if i!=n // i:
            divisors.append(n//i)

divisors.sort()
cnt = 0
num = 1
for i in range(len(divisors)):
    if num == 1:
        cnt += 1
        num *= divisors[i]
    elif gcd(num, divisors[i]) == 1:
        cnt += 1
        num *= divisors[i]

print(cnt)
