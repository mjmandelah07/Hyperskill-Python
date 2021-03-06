# Basic data types
# 1.Strings
# The string type is called str. Strings are extremely common and useful in Python. String literals may be delimited using either single or double quotes.

# Examples of strings in double quotes:
print("")  # empty string
print("string")  # one word
print("Hello, world!")  # a sentence

# Examples of strings in single quotes:
print('a')  # single character
print('1234')  # a sequence of digits
print('Bonjour, le monde!')  # a sentence

# In a real program, a string can represent an email of a person or an organization.
print('hello@hyperskill.org')  # printing an email


# 2.Numerical types
# Numbers are the most important thing for any programmer. There is hardly any serious program you can write without using numbers, so let's discuss some basic numerical types:

# i. int (signed integers). Called integers or ints, they are whole numbers (positive, negative, or zero), having no decimal point;
# ii.float (floating-point numbers). Called floats, they represent real numbers and have a decimal point.

print(11)  # prints 11
print(11.0)  # prints 11.0

# Even though 11 and 11.0 are the same number, the former is an integer, and the latter is a float. The simplest way to distinguish them is that floats have a decimal point and integers don't. Pay attention!

# You can also use negative numbers as well as zeroes:

print(0)  # prints 0
print(-5)  # prints -5
print(-1.03)  # prints -1.03

# Integer numbers can be used to count things in the real world while floating-point numbers are a good choice for statistical and scientific calculations.

# 3.Printing types
# We also have a way to clearly demonstrate types of different objects using the type() function which is a part of Python.

print(type('hello'))  # <class 'str'>
print(type("world"))  # <class 'str'>

print(type(100))  # <class 'int'>
print(type(-50))  # <class 'int'>

print(type(3.14))  # <class 'float'>
print(type(-0.5))  # <class 'float'>

# As you can see from the examples above, the type() function indicates the data type of a passed value after the word class.
