# Reading numbers from user input
# Since you have become familiar with the input() function in Python,
# it's hardly new to you that any data passed to this function is treated as a string.

integer = int(input())
floating_point = float(input())


# Free air miles
# the average amount of money per month
money = int(input("How much money do you spend per month: "))

# the number of miles per unit of money
n_miles = 2

# earned miles
miles_per_month = money * n_miles

# the distance between London and Paris
distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
print(distance * 2 / miles_per_month)

# This program will calculate how many months it takes to travel the selected distance and back.

# Advanced forms of assignment
# Naturally, similar assignment forms exist for the rest of arithmetic operations: -=, *=, /=, //=, %=, **=.
# simple assignment
number = 10
number = number + 1  # 11


# compound assignment
number = 10
number += 1   # 11


# Counter variable
#  A counter counts how many times a particular code is run.
#  It also follows that counters should be integers.

counter = 1
step = int(input("enter a number: "))  # let it be 3
counter += step
print(counter)  # it should be 4

# in case you need only non-negative integers from the user (we are increasing the counter after all!),
# you can prevent incorrect inputs by using the abs() function.

counter = 1
step = abs(int(input("enter a number: ")))  # user types -3
counter += step
print(counter)  # it's still 4
