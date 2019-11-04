N = int(input())
h = list(map(int, input().split()))

count = 0
tmp = 0
for i in range(N-1):
    if h[i] >= h[i+1]:
        count = count + 1
    else:
        count = 0

    if count > tmp:
            tmp = count

print(tmp)
