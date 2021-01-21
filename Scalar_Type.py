"""
SCALAR TYPE
It is a variable that holds a single value, that can be string, boolean, integer, float or none

the input function

the f' inside the beginning of print arbuments means that it is a formatted string literal, where {} 
"""
"""
def mult_x_and_y():
    # get some input from a user
    x = input('Input a value for x: ')

    print(f'{x} is of type {type(x)}')


    # convert that value to an int
    print('\nconverting x')

    x = int(x)
    print(f'{x} is now of type {type(x)}')

    # take in a second value and multiply the two
    y = input('\nInput a value for y: ')
    y = int(y)
    print(f'{x} * {y} = {x*y}')

mult_x_and_y()
"""

"""
FLOATING POINT NUMBER TYPE

using float function. 
Remember that floats hare stored wierdly due to precision overflow.

2 floats are considered equal only if they are stored in memory as equal. therefore, use this equal enough created function to measure the threshold difference of 2 floats

abs() is the function to return the absolute value from an operation.
"""

def equal_enough(float1, float2, difference):
    if abs(float1 - float2) < difference:
        return True
    else:
        return False

print(equal_enough(3.00001, 3.00, .01))
print(equal_enough(7.2, 7.1, .01))

'''
THE BOOLEAN TYPE

Boolean can only be True or False.

 
'''

# Some truthy values
true1 = 'hey'
true2 = 123.5
true3 = -33

true1_bool = bool(true1)
true2_bool = bool(true2)
true3_bool = bool(true3)

print(true1_bool)
print(true2_bool)
print(true3_bool)


# Some falsy values
false1 = ''
false2 = None
false3 = 0.0

false1_bool = bool(false1)
false2_bool = bool(false2)
false3_bool = bool(false3)

print(false1_bool)
print(false2_bool)
print(false3_bool)

falsity = not True
print(falsity)

def is_difference_truthly(x,y):
    z = (x - y)
    return bool(z)

print("testing")

print(is_difference_truthly(2,3))


""" 
STRING TYPE

Use len() to return the number of characters in a string.

casting an object into a string using str()

"""

"""
THE NONE TYPE

None =/= False


!= is not

"""
a = None

print(type(None))
print(a)


