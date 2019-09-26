c = list( map(int, input().split()) )
a = int( input() )

v = [1, 5, 10, 50, 100, 500]
ans = 0

for i in range(1, 7):
    t = min( a // v[-i], c[-i])
    a = a - t*v[-i]
    ans = ans + t

print(ans)