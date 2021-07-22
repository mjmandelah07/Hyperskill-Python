print("hello")

# Reading input from a user
user_name = input()
print('Hello, ' + user_name)

# clear messages
user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)

# Another way to do this is to print the message separately:
print('Enter your name: ')
user_name = input()
print('Hello, ' + user_name)

# Important details
# Here's a thing about the input() function: as soon as the program has started executing this function,
# it stops and waits for the user to enter some value and press Enter.
# That also means that if there's no input from the user, the program will not execute any further.

print("What's your favorite number?")
value = int(input())  # now value keeps an integer number

# To read several inputs, you should call the function more than once:
day = int(input())  # 4
month = input()  # October
print('my birth is', day, month)