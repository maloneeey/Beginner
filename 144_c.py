from collections import Counter
n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

div = make_divisors(n)
a = 10**12
for i in range( 0, len(div[:-1]), 2):
    a = min(a, div[i]+div[i+1])
if len(div) % 2 == 1:
    a = min(a, div[-1]*2)
print(a-2)