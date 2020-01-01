a, b = map(int ,input().split())

def calc(x):
    if x%2 == 0:
        return (x//2%2)^x
    else:
        return (x+1)//2%2
print(calc(a-1)^calc(b))