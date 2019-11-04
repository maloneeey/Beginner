n = int(input())
rest = []
for i in range(n):
    s_, p_ = input().split()
    p_ = int(p_)
    rest.append([s_, p_, i+1])

rest.sort(key=lambda x:x[1], reverse=True)
rest.sort(key=lambda x:x[0])

for i in range(n):
    print(rest[i][2])