import inspect
import math
## γ==3, ζ==6, ι==9, α==post, β==pre

def digitsum(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    print(n)

def chooseintegers():
    chooseintegers.integer_one = int(input("What is the first integer? "))
    chooseintegers.integer_two = int(input("What is the second integer? "))
    one = chooseintegers.integer_one
    two = chooseintegers.integer_two
    return one, two

def operation(int_one,int_two):
    input("Do you want to use 1.) addition, 2.) multiplication, or 3.) exponent? ")
    answer = 0
    if input == 1:
        answer = int_one + int_two
        return answer
    elif input == 2:
        answer = int_one * int_two
        return answer
    elif input == 3:
        answer = int_one ^ int_two
        return answer
    return answer
chooseintegers()
int_one = chooseintegers.integer_one
int_two = chooseintegers.integer_two
print(int_one)
print(int_two)
operation(int_one, int_two)
result = operation.answer
# digitsum(1948468113113186846)
