a, b = map(int, input().split())
for i in range(13, 1009):
    if int(i*0.08) == a and int(i*0.10) == b:
        print(i)
        exit()
print(-1)