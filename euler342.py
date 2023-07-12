from sympy.ntheory import totient as phi
from sympy.ntheory import factorint


cubes = {pow(i,3):True for i in range(1, 2155)}

def is_cube(num):
    return num in cubes

for i in range(2, 10000+1):
    n = phi(i**2)
    if is_cube(n):
        print(i, i**2, n, factorint(i))
