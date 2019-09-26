import math

def segment_sieve(a, b):
    is_prime_small = [ True for _ in range( int(math.sqrt(b))+1 )]
    is_prime = [ True for _ in range( b-a )]
    for i in range( 2, int(math.sqrt(b)) ):
        if is_prime_small[i]:
            for j in range( 2*i, int(math.sqrt(b)), i):
                is_prime_small[j] = False
            for j in range( max( 2*i, ((a+i-1)//i)*i ), b, i ):
                is_prime[j-a] = False
    return is_prime.count(True)

a, b = map(int, input().split())
print(segment_sieve(a, b))