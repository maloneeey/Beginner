n = int(input())
H = [0]+list(map(int, input().split()))+[0]
ans = 0
while max(H)>0:
    Zero = []
    for i in range(n+2):
        if H[i] == 0:
            Zero.append(i)

    for i in range(len(Zero)-1):
        if Zero[i+1] == Zero[i] + 1:
            continue
        grw = min( H[Zero[i]+1:Zero[i+1]] )
        for j in range( Zero[i]+1, Zero[i+1] ):
            H[j] -= grw
        ans += grw
print(ans)