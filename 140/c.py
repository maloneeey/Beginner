N = int(input())
b = list(map(int, input().split()))

count = b[0] + b[N-2]
for i in range(1, N-1):
    count = count + min(b[i-1], b[i])
print(count)