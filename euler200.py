from sympy.ntheory import sieve, isprime

DIGITS = [chr(ord('0') + i) for i in range(10)]

def checkStr(s):
    return "200" in s

def isPrimeProof(s):
    for i in range(len(s)):
        temp = s[i]
        for digit in DIGITS:
            if digit != temp:
                s[i] = digit
                if isprime(int(s)):
                    return False
    return True


print(DIGITS)

# Sieve primes up to LIMIT
LIMIT = 100
primes = list(sieve.primerange(2, LIMIT + 1))


data = []

for p in primes:
    for q in primes:
        if q != p:
            str_num = str(p**2 * q**3)
            if checkStr(str_num):
                data.append(str_num)
print(data)


count = 0
for num in data:
    if isPrimeProof(num):
        count += 1
        print(num, count)
    else:
        print("FAIL:", num)