from itertools import permutations, combinations
discard = set()
found = set()
cache = {}
def findSubsets(k, nums, currentSum=0, index=0):
    if k == 0:
        if currentSum in discard:
            return
        if currentSum in found:
            found.remove(currentSum)
            discard.add(currentSum)
            return
        found.add(currentSum)
        return

    if index >= len(nums):
        return

    key = (k, index, currentSum)
    if key in cache:
        return

    findSubsets(k - 1, nums, currentSum + nums[index], index + 1)
    findSubsets(k, nums, currentSum,index + 1)
    cache[key] = True


def sumAllSubsets(k, nums):
    COUNT = 0
    def helper(index, k, path):
        nonlocal COUNT
        # print(path, index, k)
        if k == 0:
            COUNT += 1
            print(path, COUNT)
            return 0
        elif index >= len(nums):
            return 0
        total = (nums[index] * len(nums) + helper(index + 1, k - 1, path + [nums[index]])
        total += helper(index + 1, k, path)

        return total

    return helper(0, k, [])


S = [i**2 for i in range(1, 101)]
B = [1,3,6,8,10,11]

print(sumAllSubsets(3, B))


testPerm = combinations(B, 3)
i = 1
total = 0
for X in testPerm:
    total += sum(X)
    print(X, i, sum(X))
    i += 1
print("Total:", total)
