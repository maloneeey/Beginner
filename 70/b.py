a, b, c, d = map(int, input().split())
start, end = 0, 0

start = a if a >= c else c
end = b if b <= d else d

time = end-start
print(time) if time > 0 else print(0)