from collections import defaultdict
from email.policy import default
import math
from collections import defaultdict


# (X+2k)^2 - (x+k)^2 - x^2 > 0
# 

# Generate first three terms of all arithmetic series
RESULTS = defaultdict(lambda:0)
LIMIT = 25
for x in range(1, LIMIT):
    for k in range(1, LIMIT):
        TOTAL = pow(x + 2*k, 2) - pow(x + k, 2) - pow(x, 2)
        RESULTS[TOTAL] += 1

RESULTS = dict(RESULTS)
keys = sorted(list(RESULTS.keys()))
for key in keys:
    print(key, RESULTS[key])




