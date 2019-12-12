from math import ceil
n = int(input())
stp = []
for _ in range(5):
    stp.append(int(input()))

stp_min = stp.index(min(stp))
tim = ceil(n/min(stp)) + 4
print(tim)