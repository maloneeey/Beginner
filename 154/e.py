from itertools import combinations
n = int(input())
k = input()
comb = list(combinations([ i for i in range(len(n))], k))