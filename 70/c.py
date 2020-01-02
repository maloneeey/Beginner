from fractions import gcd
import sys
input = sys.stdin.readline

n = int(input())
ans = 1
for _ in range(n):
    t = int(input())
    ans = ans*t//gcd(ans, t)
print(ans)