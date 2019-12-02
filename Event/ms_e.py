import sys
input = sys.stdin.readline

n = int(input())
a_ = list(map(int, input().split()))
MOD = 1000000007

cnt = 1
rbg = [0, 0, 0]

for a in a_:
    tmp = 0
    flg = 0
    for i in range(3):
        if rbg[i] == a:
            tmp += 1
            if flg == 0:
                rbg[i] += 1
            flg = 1
    cnt = cnt*tmp%MOD
print(cnt)