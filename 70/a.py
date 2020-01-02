n = input()
nn = n[-1::-1]
for i in range(len(n)):
    if n[i] != nn[i]:
        print('No')
        exit()
print('Yes')