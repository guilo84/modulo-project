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
    choice = input("Do you want to add, multiply, or exponent? ")
    if choice == "add":
        return int_one + int_two
    elif choice == "multiply":
        return int_one * int_two
    elif choice == "exponent":
        return int_one ** int_two
    else:
        print("No input")


choose_integers()
int_one = choose_integers.integer_one
int_two = choose_integers.integer_two
print(int_one)
print(int_two)
result = operation(int_one, int_two)
print(result)
print(digitsum(result))
