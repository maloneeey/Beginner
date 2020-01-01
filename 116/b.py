S = [int(input())]
ans = 0
while True:
    s = S[-1]//2 if S[-1]%2 == 0 else 3*S[-1]+1
    if s in S:
        break
    S.append(s)
print(len(S)+1)