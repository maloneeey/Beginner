from math import ceil
n, k = map(int, input().split())
A = list(map(int, input().split()))
print( ceil((n-1)/(k-1)) )