from sympy import sieve
cache = {}

def f(n):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    if n & 1: # Odd number
        cache[n] = f((n - 1) // 2)
    else:
        cache[n] = f(n // 2) + f(n // 2 - 1)
    return cache[n]

def getString(num):
    s = bin(num)[2:]
    answer = ""
    currentChar, count = s[0], 0
    for c in s:
        if c == currentChar:
            count += 1
        else:
            answer += str(count) + ","
            currentChar, count = c, 1
    answer += str(count)
    return answer
