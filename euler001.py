
# Calculates the sum of an arithmetic progression up to a given number
# startTerm = the first term of the progression
# commonDiff = the common difference of the progression
# LIMIT = the limit of the progression
# Utilizes the sum of arithmetic progression formula -> O(1)
def sumOfArithmeticProgression(startTerm, commonDiff, LIMIT):
    N = ((LIMIT - 1) - startTerm) // commonDiff + 1
    return (N * (2 * startTerm + (N - 1) * commonDiff)) // 2


LIMIT = 1000
  
# Calculates the sum of the multiples of 3 or 5 up to given limit
print(f"Summing multiples of 3 and 5 up to {LIMIT}.")
print("SUM:", sumOfArithmeticProgression(3, 3, LIMIT) + sumOfArithmeticProgression(5, 5, LIMIT) - sumOfArithmeticProgression(15, 15, LIMIT))