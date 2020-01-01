x = int(input())

def isPrime(x):
    if x == 1:
        return False
    for i in range( 2, int(pow(x, 1/2))+1 ):
        if x%i==0:
            return False
    return True

while True:
    if isPrime(x):
        print(x)
        break
    x += 1