
def genRepunits(base, LIMIT = 1000):
    repunits = []
    ones = "1"
    currentNum = int(ones, base)
    while currentNum < LIMIT:
        repunits.append(currentNum)
        ones += "1"
        currentNum = int(ones, base)
    return repunits

LIMIT = 50
hits = {}
MAX_BASE = 37
for b in range(2, MAX_BASE):
    found = genRepunits(b, LIMIT)
    for repunit in found:
        hits[repunit] = hits[repunit] + 1 if repunit in hits else 1

print(sum(num for num in hits if hits[num] > 1))
