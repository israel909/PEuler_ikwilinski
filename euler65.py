from fractions import Fraction

def digitSum(num):
    return sum(int(i) for i in str(num))

def printConvergents(data, idx = 0):
    if idx == len(data) - 1:
        return data[idx]
    else:
        return data[idx] +  Fraction(1, printConvergents(data, idx + 1))

e_list = [2, 1]
even_num = 2
for i in range(98):
    if i % 3 == 0:
        e_list.append(even_num)
        even_num += 2
    else:
        e_list.append(1)
answer = printConvergents(e_list)
print("Found Fraction:", answer)
print("ANSWER:", digitSum(answer.numerator))
