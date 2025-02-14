import inspect

class TriNum:
    def __init__(self, value):
        if value % 3 !=0:
            raise ValueError("The number is not divisible by three")
        self.value = value

class PostTriNum:
    def __init__(self, value):
        if value % 3 + 1 !=0:
            raise ValueError("The number is not divisible by three")
        self.value = value

class PreTriNum:
    def __init__(self, value):
        if value % 3 + 2 !=0:
            raise ValueError("The number is not divisible by three")
        self.value = value


integer = int(input("What is the integer? "))
divisor = int(input("What is the divisor? "))
quotient = integer % divisor
print(quotient)

# large_number_str = "12345678901234567890"
# sum_of_digits = 0
# # for digit in large_number_str:
#     sum_of_digits += int(digit)
# print(sum_of_digits)
