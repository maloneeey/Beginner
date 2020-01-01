n = int(input())
ans = 0
frc = 10

if n%2 == 0:
    while n//frc:
        ans += n//frc
        frc *= 5
print(ans)