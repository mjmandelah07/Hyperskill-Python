# 1.What is a variable?
# Variable is a named place where you can store some value and access the value later.

# For example, you calculate something and would like to reuse the formula for some other numbers. In this case, you operate only these "boxes".


# 32.Defining a variable and assigning values
# You can keep almost anything in variables just by assigning the new value for a named variable with an equal sign. Also, following PEP 8, one space before and after the assignment sign is considered good practice.

day_of_week = "Monday"
print(day_of_week)  # Monday
print(type(day_of_week))  # <class 'str'>

# Now you have a string type value "Monday" stored in computer memory. You can retrieve the value by calling the variable name.
# Now, day_of_week stores a value of the str type.


# You can always assign a new value to a defined variable:

day_of_week = "Tuesday"
print(day_of_week)  # Tuesday
# Now, you will retrieve another value:


# It is possible to assign the value of one variable to another variable:

a = 10
b = a  # b is 10
print(b)

# Python allows you to assign values of different types to the same variable.
month = "December"
print(type(month))  # <class 'str'>

# Now, let's assign the number of this month to the variable and print its type again.
month = 12
print(type(month))  # <class 'int'>

# This works because Python is a language with dynamic typing.


# 3.Naming rules
# each variable has a specific name that distinguishes it from other variables. There are some rules for naming variables that you should follow:

# Names are case-sensitive (month is not the same as Month);
# i.A name begins with a letter or an underscore, followed by letters, digits, and underscores (e.g. user_name, score1, _count);
# ii.A name cannot start with a digit (for example, 2q is not a valid name);
# iii.A name must not be a keyword.
