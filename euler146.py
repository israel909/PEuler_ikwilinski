from sympy.ntheory import isprime


def checkNum(n):
    N = pow(n,2)
    if isprime(N+1) and isprime(N+3) and not isprime(N+5):
        if isprime(N+7) and isprime(N+9) and not isprime(N+11):
            if isprime(N+13) and not isprime(N+17) and not isprime(N+19) and not isprime(N+21) and not isprime(N+23):
                if not isprime(N+25) and isprime(N + 27):
                    print(n)
                    return True
    return False

START = 10
LIMIT = 1000000
total = sum(n for n in range(START, LIMIT, 10) if checkNum(n))
print("ANSWER:", total)
