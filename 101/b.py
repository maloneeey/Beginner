n = input()
s = sum([int(i) for i in n])
n = int(n)
print('Yes') if n%s==0 else print('No')