# Creating and printing lists
# Look at a simple list that stores several names of dogs' breeds:
dog_breeds = ['corgi', 'labrador', 'poodle', 'jack russell']
print(dog_breeds)  # ['corgi', 'labrador', 'poodle', 'jack russell']

# Here is another list that contains five integers:
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

# Another way to create a list is to invoke the list function.
# It is used to create a list out of an iterable object: that is, a kind of object where you can get its elements one by one.
list_out_of_string = list('mojisola')
print(list_out_of_string)  # ['m', 'o', 'j', 'i', 's', 'o', 'l', 'a']

# Let's also note the difference between the list function and creating a list using square brackets
multi_element_list = list('danger!')
print(multi_element_list)  # ['d', 'a', 'n', 'g', 'e', 'r', '!']

single_element_list = ['danger!']
print(single_element_list)  # ['danger!']

# The square brackets and the list function can also be used to create empty lists that do not have elements at all.

empty_list_1 = list()
empty_list_2 = []

# Features of lists
# Lists can store duplicate values as many times as needed.

on_off_list = ['on', 'off', 'on', 'off', 'on']
print(on_off_list)  # ['on', 'off', 'on', 'off', 'on']
# Another important thing about lists is that they can contain different types of elements.
# So there are neither restrictions, nor fixed list types, and you can add to your list any data you want, like in the following example:

different_objects = ['a', 1, 'b', 2]

# Length of a list
# Sometimes you need to know how many elements are there in a list.
#  There is a built-in function called len that can be applied to any iterable object, and it returns simply the length of that object.
# So, when applied to a list, it returns the number of elements in that list.

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

empty_list = list()
print(len(empty_list))  # 0

single_element_list = ['danger!']
print(len(single_element_list))  # 1

multi_elements_list = list('danger!')
print(len(multi_elements_list))  # 7
