# 1.Quotes
# As you know, a string literal is surrounded by a pair of single or double quotes.
# There is basically no difference between the two, but there are some common conventions concerning their use:

# i.Use double quotes if your string contains single quotes, for example,
print("You're doing great!")

# ii.Use single quotes if your string contains double quotes, for example,
print('Have you read "Hamlet"?')

# iii.Do not mix two styles in one literal! For example, something like "string!' is not correct.

# iv.Most importantly, be consistent in your use!

# There is a way to include any quotes in your string, regardless of the style of the outer quotes, and
# that is to use the backslash symbol (\) before the quotes inside of the string.
# The backslash will basically tell Python that the quote symbol that follows it is a part of the string rather than its end or beginning.

# In the examples below, both ways of writing strings are correct and will produce the same result:

# example 1
print("You're doing great!")
print('You\'re doing great!')

# example 2
print("Have you read \"Hamlet\"?")
print('Have you read "Hamlet"?')

# 2.Multiline strings
# Strings can represent a long text, a single character, or even no characters, like in the case of an empty string.
# One thing has so far been true about all of them: all our strings were single line, no matter how long they were.
# However, you can also write multi-line strings in Python! To do that, you need to use triple quotes on each side of the string literal.
# Again, the choice of single or double quotes is up to you as both work fine in Python.

# Multi-line string in double quotes:

print("""This
is
a
multi-line
string""")

# Multi-line string in single quotes:

print('''This
is
a
multi-line
string''')
