
# Sums the even fibonacci numbers until the sum is greater than the given limit
def even_fibonacci_sum(LIMIT):
    a, b = 0, 1
    sum = 0
    while a < LIMIT:
        a, b = b, a + b
        sum += a if a % 2 == 0 else 0
    return sum

LIMIT = 4000000
print(f"Summing even fibonacci numbers up to {LIMIT}.")
print("SUM:", even_fibonacci_sum(LIMIT))