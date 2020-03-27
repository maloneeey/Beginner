h, w = map(int, input().split())
S = [ [s for s in input()] for _ in range(h) ]
flag = True
for y in range(h):
    for x in range(w):
        if S[y][x] == '#':
            flag = False
            if y > 0 and S[y-1][x] == '#': flag = True
            if y < h-1 and S[y+1][x] == '#': flag = True
            if x > 0 and S[y][x-1] == '#': flag = True
            if x < w-1 and S[y][x+1] == '#': flag = True
        if flag == False:
            print('No')
            exit()
print('Yes')