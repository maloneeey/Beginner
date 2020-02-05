h, w = map(int, input().split())
S = [ '.'*(w+2) ]
for _ in range(h):
    s = '.' + input() + '.'
    S.append(s)
S.append( '.'*(w+2) )

def 