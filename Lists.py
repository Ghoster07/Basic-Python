"""
LISTS

"""

# Here are different ways to call lists into your code

empty_list = list()
empty_list = []

# Lists can be inside other lists, this is called nesting

list_of_mixed_types = [True, 14, 'cat', [76, 33.3]]
print(list_of_mixed_types)

# Concatenating lists
first_list = ['This', 'is', 'list', '1']
second_list = ['add', 'me', 'to', 'list', '1']

concatenated_list = first_list + second_list

print(concatenated_list)

print(type(concatenated_list))

cat = "cat"
print(cat*2)

"""
THE RANGE FUNCTION

"""

start = 0
stop = 10
step = 2

# Prints the numbers 0, 2, 4, 6, 8 each on a new line
for num in range(start, stop, step):
    print(num)

# The default for start is 0 inclusive, and step default is 1 non-inclusive. The stop number will stop before hitting the actual number.

print(list(range(10)))

"""
ACCESSING LIST VALUES

"""
print(first_list)
print(first_list[0])
print(first_list[-1])

animal_list = ['cat', 'dog', 'bird', 'horse']

# Prints the animals in index 0, 1, -1 from the list
print(f'the first animal in the list is {animal_list[0]}')
print('the second animal in the list is {}'.format(animal_list[1]))
print('the last animal in the list is {}'.format(animal_list[-1]))

# This is a way to change a part of a list
animal_list = ['platypus', 'beaver', 'hawk']

animal_list[0] = 'dolphin'

# Prints "dolphin"
print(animal_list)


"""
THE DEL FUNCTION
"""
my_list=list(range(10))
print(my_list)
del my_list[0]
print(my_list)

"""
"unpacking"
 Normaly tuples are unpacked, but lists can do so as well


"""
# A list with three cat breeds
cat_list = ['bengal', 'siamese', 'sphinx']

# Unpacking the list into three new variables (cat1, cat2 and cat3),
# which is equal to the number of elements within cat_list
cat1, cat2, cat3 = cat_list

print(f'{cat1} {cat2} {cat3}')

"""
LIST MEMBERSHIP

The in Keywhord is used to check whether an element is in a list.

"""
print(cat2 in cat_list)

"""
The not in works the exact opposite
"""

"""
ACCESSING A PORTION OF A LIST

list[start:stop]
start will be included, but not the stop.

"""
a = 20
n = 40

num_list = list(range(a, n))

print(num_list[0:5])
print(num_list[10:])
print(num_list[7:14])

# Note that element at index -1 is not shown when slicing num_list
# up until that index
print(num_list[-1])
#from the 7th one to the 1st one, counting from the end backwards.
print(num_list[-7:-1])

"""
Remember that editing a sublist need to be done when this is assigned to a separate variable from the original list.

some_list[start:stop:step]

"""
a = 10
n = 20

num_list = list(range(a, n))

num_sublist = num_list[0:5]

num_sublist[0] = 900

# Notice the 0th index is only changed in the sublist
print(num_list[0])
print(num_sublist[0])

humans_and_animals = ['Brad Pitt', 'seagull', 'Sammy Davis Jr', 'cat', 'Thurston Moore', 'crane']

# Prints every other item starting at index 1
animals = humans_and_animals[1:len(humans_and_animals):2]
print(animals)

#setting a list backwards
humans_and_animals_backwards = humans_and_animals[::-1]
print(humans_and_animals_backwards)
print(humans_and_animals[4:1:-1])

print(humans_and_animals[::-2])


"""
NESTED LISTS 

Lists, sublists and sub-sublists
"""
nested_list = [['a', 'b', 'c'], [1, 2, 3]]

# Use indexing to access the second element in the first nested list
element_within_nested_list = nested_list[0][1]
print(element_within_nested_list)


