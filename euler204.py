import math
import heapq
from sympy.ntheory import sieve
import copy

def countHammingNumbers(type, LIMIT):
    availablePrimes = list(sieve.primerange(2, type + 1))

    def getHammingNumber(state):
        return math.prod(availablePrimes[i]**state[i] for i in range(len(state)))


    count = 1
    pq  = []
    visited = set()
    for i in range(len(availablePrimes)):
        state = [0] * len(availablePrimes)
        state[i] = 1
        visited.add(tuple(state))
        heapq.heappush(pq, (getHammingNumber(state), state))

    while len(pq) != 0:
        num, state = heapq.heappop(pq)
        if num > LIMIT:
            break
        print(num)
        count += 1

        for i in range(len(availablePrimes)):
            newState = copy.copy(state)
            newState[i] += 1
            temp = tuple(newState)
            if temp not in visited:
                visited.add(temp)
                heapq.heappush(pq, (getHammingNumber(newState), newState))

    return count  


answer = countHammingNumbers(100, 10**9)
print("Answer:", answer)