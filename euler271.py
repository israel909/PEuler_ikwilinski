from sympy.ntheory import factorint

cache = {}
def S(n):
    if n in cache:
        return cache[n]
    vals = [x for x in range(2, n) if pow(x,3,n) == 1]
    cache[n] = (sum(vals), vals)
    return cache[n]

for i in range(2, 101):
    out, vals = S(i)
    if out == 0:
        print(f'S({i}) = 0')
    else:
        print(f'S({i}) = {out}\t{vals}\t{sum(S(x)[0] for x in vals) + vals[-1]}')
