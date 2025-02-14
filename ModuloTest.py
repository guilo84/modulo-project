import inspect
import math


def digitsum(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    print(n)


# integer = int(input("What is the integer? "))
# divisor = int(input("What is the divisor? "))
# quotient = str(integer % divisor)
#
# print(quotient)
digitsum(19)
