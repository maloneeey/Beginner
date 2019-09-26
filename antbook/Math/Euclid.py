def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

p1 = list( map(int, input().split()) )
p2 = list( map(int, input().split()) )

print(gcd(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))-1)