n, k = map(int, input().split())
lr = list(input())
j = 0
counts = [0]
for i in range(n):
    if lr[j] == lr[i]:
        counts[-1] += 1
    else:
        j = i
        counts.append(1)

for _ in range(k):
    if len(counts)>=3:
        counts[0] += counts[1]+counts[2]
        del counts[1:3]
    elif len(counts)==2:
        counts[0] += counts[1]
        del counts[1]
    else:
        break

count = sum(counts) - len(counts)
print(count)