# Comparison operators
# Comparison or relation operations let you compare two values and determine the relation between them.
# There are ten comparison operators in Python:
# < strictly less than
# <= less than or equal
# > strictly greater than
# >= greater than or equal
# == equal
# != not equal
# is object identity
# is not negated object identity
# in membership
# not in negated membership.


# Comparing integers
# In this topic, we will cover only integer comparison

a = 5
b = -10
c = 15

result_1 = a < b   # False
result_2 = a == a  # True
result_3 = a != b  # True
result_4 = b >= c  # False
print(result_1)
print(result_2)
print(result_3)
print(result_4)

# Any expression that returns an integer is a valid comparison operand too:

a = 5
b = -10
c = 15

calculated_result = a == b + c  # True
print(calculated_result)

# Given the defined variables a, b and c, we basically check if 5 is equal to -10 + 15, which is true.

x = -5
y = 10
z = 12

result = x < y and y <= z  # True
print(result)

a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

print(b + c <= e or f + g >= e == f == 5)
print((b + c <= e or f + g >= e) == (f == 5))  # True

# logic & ARITHMETIC
# True and-expressions return the result of the last operation:
print(b + c * f >= e and (f + g) * c)  # 33
print((f + g) * c and b + c * f >= e)  # True

# False and-expressions return a boolean False value:
print(b + c * f <= e and (f + g) * c)  # False
print((f + g) * c and b + c * f <= e)  # False

# True or-expressions return the result of the first operation:
print(b + c * f >= e or (f + g) * c)  # True
print((f + g) * c or b + c * f >= e)  # 33

# True-False or-expressions return the True part:
print((f + g) * c or b + c * f <= e)  # 33
print(b + c * f <= e or (f + g) * c)  # 33


