N = int(input())
v = list(map(int, input().split()))

v_ = sorted(v)

half = v_[0]
for i in range(1, len(v)):
    half = ( half + v_[i] ) / 2
print(half)