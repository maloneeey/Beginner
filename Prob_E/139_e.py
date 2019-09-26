from collections import deque

N = int(input())
a = [list(map(int, input().split())) for a in range (N)]
que = []
flag = [0]*N
count = 0
for i in range(N):
    que.append(deque(a[i]))

while que:
    flagRound = 0
    for i in range(N):
        if flag[i] == 1:
            flag[i] = 0
            continue

        if que[que[i][0]-1][0]-1 == i:
            que[i].popleft()
            que[ que[i][0]-1 ].popleft()
            flag[ que[i][0]-1 ] = 1
            flagRound = 1

    if flagRound == 0:
        print(-1)
        break

    count = count + 1

if flagRound == 1:
    print(count)