from itertools import combinations, permutations
from collections import deque
from fractions import Fraction
import copy

def solver(digits):
    data = set()
    Q = deque()
    for d in digits:
        L = copy.copy(digits)
        L.remove(d)
        Q.append([Fraction(d, 1), L])

    while len(Q) != 0:
        val, remaining = Q.popleft()
        if len(remaining) == 0:
            if val > 0 and (isinstance(val,int) or val.denominator == 1):
                data.add(int(val.numerator))
            continue

        for r in remaining:
            L = copy.copy(remaining)
            L.remove(r)
            Q.append([val + r, L])
            Q.append([val - r, L])
            Q.append([val * r, L])
            Q.append([val / r, L])
            Q.append([r - val, L])
            if val != 0:
                Q.append([r / val, L])

    return sorted(list(data))


def check(nums):
    if nums[0] != 1:
        return 0
    count = 1
    for x in nums:
        if x == count:
            count += 1
        else:
            break
    return count - 1


arr = list(combinations(list(range(1, 10)), 4))
best = 0
answer = None
for c in arr:
    X = [x for x in c]
    data = solver(X)
    T = check(data)
    print(c, T, max(data))
    if T > best:
        best = T
        answer = c

answer = list(map(str, answer))
print("ANSWER:", ''.join(answer))
