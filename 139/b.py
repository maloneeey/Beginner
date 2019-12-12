a, b = map(int, input().split())

count = 0
plug = 1

while plug < b:
    plug = plug + a - 1
    count = count + 1

print(count)
