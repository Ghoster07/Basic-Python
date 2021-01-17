# Hello

some_string = ''' Hello, this one can be used to type on multiple lines 
'''

some_other_string = """ 
Hello, th newline character is invisible, both lines are strings, and can be printed
"""

print (some_string, some_other_string)

def reverse_a_string(input_str):
  """ 
  This function will output a reversed string from an input some_other_string
  """

  reverse_str = ""
  for i in reversed(range(len(input_str))):
    reverse_str += input_str[i-1]

  return reverse_str

print(reverse_a_string(some_other_string))

def do_something_with(some_parameter):
  altered_param = some_parameter
  altered_param += 1
  return altered_param

print(do_something_with(7))


""""
TYPES AND CLASSES

An integer 'int' are normally discrete values

A float is a value with decimal point "think about it like this for now" precision is finite

True and False are 'bool' boolean, a data type that can have one or two values

"""

print(type(False))


"""
COMMON ARITHMETIC OPERATORS

+, -, *, /

When you do an operation with decimals, you can lead to precision errors, because there is a finite number of bits allocated to decimals, divisions end up producing a float

"""


print(7 / 3)

"""
// floor division round down during a division
** power of some number, this "2^3" means something else in python
% calculando el restante de x dividido por y x%y, can be used to calculate whether a number is even or odd

== is equal to 

//,**,%
"""

print(7%2 == 1)
print(type(some_other_string))
print(6 - 3.0 == 3)

"""
ORDER OF OPERATIONS 
just remmember PEMDAS
"""

print(float(27))
# The int function will round down the float inpunt
print(int(13.99))
# any value which is not 0 wil
print(bool(0.0))


'''
VARIABLES
'''

x = "some string"

y = 521 / 74 + 7**(1/8)
print(y)


'''
INCREMENTING OPERATION
+=, *=, /=
'''

'''
When Scalar Type Variable Change
'''
# Immutable type
#   int, float, boolean, string, tuple

x = 27
print ("x: ", id(x))

y = 27
print("y: ", id(y))

x += 3
y += 3
print("x: ", id(x))
print("y: ", id(y))

def reverse_a_string(input_str):
    """Returns the reversed input string.

    Parameters
    ----------
    input_str : str
        The string to be reversed.

    Returns
    -------
    reverse_str : str
        The result of reversing the string.

    """
    reverse_str = ''
    for i in range(len(input_str)-1,-1,-1):
        reverse_str += input_str[i]

    return reverse_str


print(reverse_a_string('I am excited to turn it around'))

# Python correctly interprets the line below as two separate statements
# but it may be confusing to other people reading your code
x = 5; print("Hello, world!")

def divisible_by_3_or_5(n):
  if n % 3 == n % 5 == 0:
   print(n, " is divisible by both 3 or 5")
  elif n % 3 == 0:
    print( n, " is divisible by 3")
  elif n % 5 == 0:
    print (n , " is divisible by 5")
  else:
    print( n, " is divisible by neither 3 or 5")
  
divisible_by_3_or_5(30)

"""
Printing vs return
Every function will return "None, even if you don't return anything. None is the absence of a value in python
"""

def a_function(n):
  return(n + 2)


def simple_func(x,z):
  y=x
  y += z
  y //= 2

  y = a_function(y)

  return 5*y
  
print(simple_func(6,7))

print (11%5*6)
print((11%5)*6)
