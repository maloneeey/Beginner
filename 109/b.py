n = int(input())
W = []
for _ in range(n):
    w = input()
    if w in W:
        print('No')
        exit()
    W.append(w)

for i in range(n-1):
    if W[i][-1] != W[i+1][0]:
        print('No')
        exit()
print('Yes')