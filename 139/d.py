N = int(input())
count = int( (N-1) / 2 )

if (N-1) % 2 == 0:
    intSum = N*count
else:
    intSum = N*count + count + 1

print(intSum)