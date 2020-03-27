A = [ list(map(int, input().split())) for _ in range(3) ]
n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0
flag = False
for i in range(3):
    if sum( [ A[i][j] for j in range(3)] ) == 0:
        flag = True
    if sum( [ A[j][i] for j in range(3)] ) == 0:
        flag = True
if sum( [A[i][i] for i in range(3)] ) == 0 or sum( [A[2-i][i] for i in range(3)] ) == 0:
    flag = True
print("Yes") if flag else print("No")