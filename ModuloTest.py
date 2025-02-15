import inspect
import math
## γ==3, ζ==6, ι==9, α==post, β==pre

def digitsum(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def choose_integers():
    choose_integers.integer_one = int(input("What is the first integer? "))
    choose_integers.integer_two = int(input("What is the second integer? "))
    # one = choose_integers.integer_one
    # two = choose_integers.integer_two
    return choose_integers.integer_one, choose_integers.integer_two

def operation(int_one,int_two):
    choice = input("Do you want to 1.) add, 2.) multiply, or 3. raise to an exponent? ")
    if choice == "1":
        return int_one + int_two
    elif choice == "2":
        return int_one * int_two
    elif choice == "3":
        return int_one ** int_two
    else:
        print("No input")

def divisibility(value):
    if value % 6 == 0:
        return "six"
    elif value % 9 == 0:
        return "nine"
    elif value % 3  == 1:
        return "post"
    elif value % 3  == 2:
        return "pre"
    elif value % 3 == 0:
        return "triNum"


choose_integers()
int_one = choose_integers.integer_one
int_two = choose_integers.integer_two
result = operation(int_one, int_two)


print("The first integer",int_one," is a",divisibility(int_one))
print("The second integer",int_two," is a",divisibility(int_two))
print("The result of the operation is",result)
print("The ulitmate sum of all digits is", digitsum(result))
print("The number",digitsum(result), "is a",divisibility(digitsum(result)))
