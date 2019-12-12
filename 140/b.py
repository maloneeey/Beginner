N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

point = 0
for i in range(N):
    point = point + b[i]

for i in range(1, N):
    if a[i] == a[i-1] + 1:
        point = point + c[ a[i-1]-1 ]

print(point)