import math

FACES = 6
dp = {}
def countWays(index, target):
    if index == 0:
        return 1 if target == 0 else 0
    if target < 0:
        return 0
    
    key = (index, target)
    if key in dp:
        return dp[key]
    

    ways = 0
    for i in range(1, FACES + 1):
        ways += countWays(index - 1, target - i)
    dp[key] = ways
    return ways


answer = countWays(5, 15)
print("Answer:", answer)
