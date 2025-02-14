import inspect



integer = int(input("What is the integer? "))
divisor = int(input("What is the divisor? "))
quotient = str(integer % divisor)

print(quotient)

number_str = quotient
sum_of_digits = 0
for digit in number_str:
    sum_of_digits += int(digit)
print(sum_of_digits)
