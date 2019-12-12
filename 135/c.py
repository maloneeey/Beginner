n = int(input())
a = list( map(int, input().split()) )
b = list( map(int, input().split()) )

cnt = 0
for i in range(n):
    monster = min(a[i], b[i])
    a[i] -= monster
    b[i] -= monster
    cnt += monster

    monster = min(a[i+1], b[i])
    a[i+1] -= monster
    b[i] -= monster
    cnt += monster

print(cnt)