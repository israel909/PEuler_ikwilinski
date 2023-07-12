import math
from math import prod
from sympy.ntheory import factorint
from sympy import sieve, prime


def factor_n_factorial(n):
    if n == 0:
        return {}
    if n == 1:
        return {1:1}
    primes = [i for i in sieve.primerange(2, n + 1)]
    facorization = {}
    for prime in primes:
        power = sum(math.floor(n / pow(prime, i)) for i in range(1, int(math.log(n, prime)) + 1))
        facorization[prime] = power
    return facorization

def cancel_factoriazation(larger_fact, smaller_fact):
    for prime in smaller_fact:
        larger_fact[prime] -= smaller_fact[prime]
        if larger_fact[prime] == 0:
            del larger_fact[prime]
    return larger_fact

def solve(n, k):
    A = factor_n_factorial(n)
    B = factor_n_factorial(k)
    cancel_factoriazation(A, B)
    other_term = factor_n_factorial(n - k)
    cancel_factoriazation(A, other_term)
    return sum(prime * A[prime] for prime in A)

print("ANSWER:", solve(20000000, 15000000))
