n = int( input() )
r = int( input() )
x = list( map( int, input().split() ) )

x = sorted(x)

i = 0
ans = 0
while i < n:
    s = x[i]
    i = i + 1
    while i < n and x[i] <= s + r:
        i = i + 1

    p = x[i-1]
    while i < n and x[i] <= p + r:
        i = i + 1

    ans = ans + 1

print(ans)