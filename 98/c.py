n = int(input())
s = input()
cnt = 0
W, E = [], []
w, e = 0, 0
for i in range(n):
    W.append(w); E.append(e)
    if s[i] == 'W':
        w += 1
    if s[-i-1] == 'E':
        e += 1
print(min([w+e for (w, e) in zip(W, E[::-1])]))