N = int(input())
s =[]
count = 0

for i in range(N):
    tmp = list( input() )
    tmp.sort()
    tmp = ''.join( tmp )
    s.append( tmp )

    for j in range(i-1):
        if s[i] == s[j]:
            count = count + 1

print(count)

