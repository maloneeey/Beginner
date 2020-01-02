n = int(input())

def dfs(x):
    if x>n:
        return 0
    cnt = 1 if all(str(x).count(a) > 0 for a in '753') else 0
    for a in '753':
        cnt += dfs( int(str(x)+a) )
    return cnt
print(dfs(0))