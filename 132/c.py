n = int(input())
d = sorted(list(map(int, input().split())))
print( d[int(n/2)]-d[int(n/2)-1] )