import math
def is_prime(n):
    i = 2
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return n != 1

def divisor(n):
    q = []
    for i in range(1, int(math.sqrt(n))):
        if n%i == 0:
            q.append(i)
            if i != n%i:
                q.append( int(n/i) )
    return sorted(q)

def prime_factor(n):
    res = [ 0 for _ in range( n+1 )]
    for i in range(2, int(math.sqrt(n))):
        while n%i == 0:
            res[i] += 1
            n /= i
    if n != 1:
        res[int(n)] = 1

    for i in range(2, int(math.sqrt(n))):
        poly = []
        if res[i] != 0:
            poly.append( str(i)+"*"+str(res[i]) )
    return poly



n = int(input())
string = "Yes" if is_prime(n) else "No"
print(string)
print(divisor(n))
print(prime_factor(n))