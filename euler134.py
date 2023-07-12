from sympy.ntheory import sieve


# Last digits must be of p whilst also being also divisible by q
# Return the smallest number that satisfy the above
def findMin(p, q):
    numStr = str(p)
    for i in range(1, 10**7):
        X = int(str(i) + numStr)
        if X % q == 0:
            return X
    print("FAILED TEST CASE FOR:", p, q)
    return -1
    

# Sieve the primes up to MAX + 1
MAX = 10000
primes = list(sieve.primerange(1, MAX + 1))
primes = primes[2:]

answer = 0
for i in range(len(primes) - 1):
    res = findMin(primes[i], primes[i + 1])
    assert res != -1
    answer += res
    # print(primes[i], primes[i + 1], res, answer)

print("Answer:", answer)