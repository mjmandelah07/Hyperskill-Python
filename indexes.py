# Indexes of elements
# To access an element of a list by its index, you need to use square brackets.
# You add the brackets after the list and, between them, you write the index of an element you want to get.
# Don't forget, the indexes start at 0, so the index of the first element is 0.
# The index of the last element is equal to len(list) - 1.
# Let's take a look at the example below:
#
# colors = ['red', 'green', 'blue']
#
# first_elem = colors[0]   # 'red'
# second_elem = colors[1]  # 'green'
# third_elem = colors[2]   # 'blue'
# Strings work in the same way:
#
# pet = "cat"
#
# first_char = pet[0]   # 'c'
# second_char = pet[1]  # 'a'
# third_char = pet[2]   # 't'


# There is one more obstacle in your way. Imagine that you want to change one of the elements in a list.
#  It can be easily done:
# colors = ['red', 'green', 'blue']
color = ['red', 'green', 'blue']
color[1] = 'white'
print(color)

# Negative indexes
# The easier way to access the elements at the end of a list or a string is to use negative indexes:
# the minus before the number changes your perspective in a way and you look at the sequence from the end.
# the last element of a list, in this case, has the index equal to -1,
# and the first element of the list has the index So, -len(list) (the length of the list).
# #
# For example:
#
# colors = ['red', 'green', 'blue']
#
# last_elem = colors[-1]    # 'blue'
# second_elem = colors[-2]  # 'green'
# first_elem = colors[-3]   # 'red'
#
# pet = "cat"
#
# last_char = pet[-1]    # 't'
# second_char = pet[-2]  # 'a'
# first_char = pet[-3]   # 'c'
# As you can see, it works the same for lists and strings.
