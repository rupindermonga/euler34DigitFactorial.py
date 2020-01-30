#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def factors(n):
    rem = 1
    final_list = []
    while n !=0:
        rem = n % 10 
        n = int(n // 10)
        #if rem != 0:
        final_list.append(rem)
    return final_list

def ListFactorial(n):
    final_sum = 0
    while n >0:
        final_sum += math.factorial(n % 10)
        n = int(n//10)
    return final_sum


def DigitFactorial():
    sum = 0
    d = 1
    while math.factorial(9)*d > 10**d:   
        d += 1
    for a in range(3, math.factorial(9)*d):
        if ListFactorial(a) == a:
            sum += a
    return sum


final = DigitFactorial()
print(final)