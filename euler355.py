from sympy.ntheory import factorint
from sympy import sieve

def maximalCoprimeSubset(LIMIT):
    '''
    Finds the maximal coprime subset of positive integers upto LIMIT
    '''
    # Initialize the list of primes
    primes = list(sieve.primerange(2, LIMIT))
    
    def helper(index):
        if index >= len(primes):
            return 0
        
        # Either choose the prime or not
        A = primes[index] + helper(index+1)
        B = helper(index+1)

    return primes

print(maximalCoprimeSubset(10))