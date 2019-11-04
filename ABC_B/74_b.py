n = int(input())
k = int(input())
x = list(map(int, input().split()))

dist = 0
for i in x:
    dist += 2*min( abs(k-i), i )
print(dist)