import numpy as np
from math import gcd
from sympy.ntheory import factorint

def test_e_value(e, n, best):
    count = 2
    for m in range(2, n):
        if pow(m, e, n) == m:
            # print(m, e)
            count += 1
            if count > best:
                return np.inf
    return count

def solve(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    best = np.inf
    answer = 0
    print(n, phi)
    for e in range(2, 1000, 2):
        print(e)
        if gcd(e, n) == 1:
            value = test_e_value(e, n, best)
            if value < best:
                print("Found a new best:", e)
                print("Current best of:", value)
                best = value
                answer = e
            elif value == best:
                print("Got a value of", e, factorint(e))
                answer += e
    return answer


print(solve(1009, 3643))
print(test_e_value(2, 1009 * 3643, np.inf))
