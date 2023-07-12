from sympy.ntheory import sieve
import math
import time

NUM_CUBES_TO_GENERATE = 1000
CUBES = [pow(n,3) for n in range(1, NUM_CUBES_TO_GENERATE + 1)]
start = 0

def isPerfectCube(num):
    return round(math.pow(num,1/3))**3 == num

def testPrime(prime):
    global start
    for i in range(start, len(CUBES)):
        cube = CUBES[i]
        num = pow(cube,3) + pow(cube, 2)*prime
        if isPerfectCube(num):
            print(f'{cube}^3 + {cube}^2*{prime} = {round(math.pow(num, 1/3))}^3 = {num}')
            start = i
            return True
    return False


# Sieve the first primes up to the given limit
LIMIT = 1000000
primes = list(sieve.primerange(2, LIMIT))

start = time.time()
answer = sum(1 for prime in primes if testPrime(prime))
end = time.time()
print("Answer:", answer)
print("Time:", end - start, "seconds")