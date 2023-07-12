from sympy.ntheory import isprime
import numpy as np

# Returns the nth triangular number
def t(n):
    return n*(n+1)//2

def getMinAndMax(n):
    return t(n) + 1, t(n) + n + 1


def isPrimeTriplet(n, idx, currentNum):
    # If idx == 0
    count = 0
    ABOVE_START_NUM, ABOVE_END_NUM = getMinAndMax(n - 1)
    BELOW_START_NUM, BELOW_END_NUM = getMinAndMax(n + 1)

    ABOVE, BELOW, LEFT, RIGHT = 0, 0, 0, 0
    ABOVE_LEFT, ABOVE_RIGHT, BELOW_LEFT, BELOW_RIGHT = 0, 0, 0, 0

    if idx <= n - 1:
        ABOVE = ABOVE_START_NUM + idx
        RIGHT = currentNum + 1
        if idx <= n - 2:
            ABOVE_RIGHT = ABOVE + 1

    BELOW = BELOW_START_NUM + idx
    if idx > 0:
        LEFT = currentNum - 1
        ABOVE_LEFT = ABOVE_START_NUM + idx - 1
        BELOW_LEFT = BELOW - 1
    BELOW_RIGHT = BELOW + 1

    print("CURRENT:", currentNum)
    print(ABOVE, BELOW, LEFT, RIGHT)
    print(ABOVE_LEFT, ABOVE_RIGHT, BELOW_LEFT, BELOW_RIGHT)
    #print()
    
    # Check if at least 2 of the 8 numbers are prime
    if isprime(ABOVE):
        count += 1
    if isprime(BELOW):
        count += 1
    if isprime(ABOVE_LEFT):
        count += 1
    if isprime(ABOVE_RIGHT):
        count += 1
    if isprime(BELOW_LEFT):
        count += 1
    if isprime(BELOW_RIGHT):
        count += 1
    return count == 2
        
    

def S(n):
    if n == 1:
        return 0
    if n == 2:
        return 5
    start_num, end_num = getMinAndMax(n)
    answer = 0
    idx = 0
    for num in range(start_num, end_num + 1):
        if isprime(num):
            if isPrimeTriplet(n, idx, num):
                answer += num
        idx += 1
    return answer

print(S(9 - 2))


