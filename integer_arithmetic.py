# 1.Basic operations
# Python supports basic arithmetic operations:
#
# addition +
# subtraction -
# multiplication *
# division /
# integer division //
# The examples below show how it works for numbers.
print(10 + 10)
print(100 - 10)
print(10 * 10)
print(77 / 10)
print(77 // 10)

# 2.Writing complex expressions
# Arithmetic operations can be combined to write more complex expressions:

print(2 + 2 * 2)  # 6

# To specify an order of execution, you can use parentheses, as in the following:

print((2 + 2) * 2)  # 8

# The minus operator has a unary form that negates the value or expression.
# A positive number becomes negative, and a negative number becomes positive.

print(-10)  # -10
print(-(100 + 200))  # -300
print(-(-20))  # 20

# Other operations
# The remainder of a division. Python modulo operator % is used to get the remainder of a division.
# It may come in handy when you want to check if a number is even.
# Applied to 2, it returns 1 for odd numbers and 0 for the even ones.
print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number

# Here are some more examples:

# Divide the number by itself
print(4 % 4)  # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)  # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)  # 4
print(11 % -5)  # -4
print(-24 % 3)
print(-24 % 5)

# Exponentiation. Here is a way to raise a number to a power:
#
print(10 ** 2)  # 100
# This operation has a higher priority over multiplication.

# Operation priority
# To sum up, there is a list of priorities for all considered operations:
#
# parentheses
# power
# unary minus
# multiplication, division, and remainder
# addition and subtraction
# As mentioned above, the unary minus changes the sign of its argument.
#
# Sometimes operations have the same priority:
#
print(10 / 5 / 2)  # 1.0
print(8 / 2 * 5)  # 20.0

print(2 ** 179)

n = 1234567890
m = 987654321
x = 67890
y = n * m
z = y + x
print(z)

n = 31 ** 331
m = n % 20
print(m)