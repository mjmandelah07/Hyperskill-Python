# 1.            The Hello World program
# Here, print is the name of a function. A function is a block of code that does some useful work for you, e.g. prints a text.
# In some sense, a function is a subprogram that can be reused within your programs.
# When the name of a function is followed by parentheses, it means that it was called to get the result.
# "Hello, World!" is a Python string. All strings are surrounded by either single or double quotes, so 'Hello, World!' is also a valid string.

# You may replace this string with another one, and the program will print the new string.
# e.g
print('Python 3.x')


# 2.           PRINTING QUOTES
# In some sense, a function is a subprogram that can be reused within your programs.
#  e.g
print("Yes, I'm ready to learn Python.")


# Part of the string with I'm is printed correctly, because you used double quotes "..." to enclose the whole string:

# Yes, I'm ready to learn Python.


# If you write it in the following wrong way:

print('Yes, I'
m
ready
to
learn
Python.
')

# your program won't know where the string starts and ends.


# 3.Possible errors
# Even this simple line of code may contain errors, most common of them are:

# (i).Putting extra indentation

print("Hello, World!")

# This does not work because of extra spaces before print.

# (ii).Calling the function by the wrong name


pint("Hello, World!")

# This line contains pint instead of print. Make sure to refer to every function by its proper name.

# (iii).Writing names in the wrong case

PRINT("All caps")

# Again, Print, print and PRINT are not the same. Names are case-sensitive in Python.

# (iv).Missing one or both quotes for a string

print("Python)

# This does not work because of missing closing quotes.

# (v).Missing one or more parentheses

print("I have no end"

# Be careful with parentheses, especially when calling a function.
