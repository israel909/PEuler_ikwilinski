

dp = {}
def f(K):

    class Solution:
        def __init__(self, K):
            self.G = 2 * K
            self.K = K

        def solver(self, k, currentNum, left, right):
            if k == 0 and left == right:
                self.G = min(self.G, right)
                return 0
            elif k == 0:
                return float("inf")
            if left > right:
                return float("inf")
            if right >= self.G:
                return float("inf")
            key = (k, currentNum, left, right)
            if key in dp:
                return dp[key]
            best = float("inf")
            for i in range(currentNum, self.K + 1):
                candidate = None
                if left == 0:
                    candidate = i + self.solver(k - 1, i, i, i)
                else:
                    if left * i > right + i:
                        break
                    elif left * i > self.G:
                        break
                    candidate = i + self.solver(k - 1, i, left * i, right + i)
                if candidate < best:
                    best = candidate
            dp[key] = best
            return dp[key]

        def findAnswer(self):
            return self.solver(self.K, 1, 0, 0)


    S = Solution(K)
    return S.findAnswer()


prod_nums = set()
LIMIT = 1000
for i in range(2, LIMIT + 1):
    X = f(i)
    print(f"f({i}) = {X}")
    prod_nums.add(X)

print()
print("ANSWER:", sum(prod_nums))
