abc = list(map(int, input().split()))
k = int(input())
print( sum(abc)+max(abc)*(2**k-1) )