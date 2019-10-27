n = int(input())

flg = 0
for i in range(1, 10):
    for j in range(1, 10):
        if n == i*j:
            flg = 1
print("Yes" if flg else "No")