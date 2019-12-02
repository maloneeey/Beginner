n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = 0
srt_a = sorted(a)
srt_b = sorted(b)
for i in range(n):
    if srt_b[i]-srt_a[i] < 0:
        flag = 1
        break

for 