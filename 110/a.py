Abc = list(map(int, input().split()))
ans = 0
for i in range(len(Abc)):
    ans = max( Abc[i]+Abc[(i+1)%3]+Abc[(i+2)%3]*10, ans )
print(ans)