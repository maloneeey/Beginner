n, d = map(int, input().split())
i = 0
count = 0
while i<n:
    i += 1+2*d
    count += 1
print(count)