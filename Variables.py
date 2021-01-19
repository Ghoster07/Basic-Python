"""
OVERVIEW

Essentially, you give a a name to something so that it can be accessed later. Making less tedious but higher-level thinking.

WHAT IS A VARIABLE

The example bellow represents the word apple as a variable for the integer 20
"""
apple = 20
print(apple)

"""
By replacing the values associated to a variable makes code reusable and easier to implement changes

variable = value

you can also declare multiple variables on the same line

"""

x, y = 1, 2

print(x)
print(y)

"""
It is also possible to assign multiple variables from a sequence: UNPACKING
"""

x = (1,2,3)
a,b,c = x
print(c,b,a)

"""
Assigning multiple variables to a same value
"""
a = b = c = 0

print(a,b,c)

x = a, b, c
print(x)


"""
VARIABLE TYPES

You can discover the type of a variable by using type(), however, you can also use is instance(object, type) to ask if an object of a specific type

type (x) == int and isinstance(x, int) has basically the same output


"""

x = 1

print(type(x) == int)

print(isinstance(x,int))

z = 7 == 3
print (type(z))

y = 3//2
print(type(x))

"""
MUTABILITY

When a variable mantains memory address reference even after changes of the value referred to that variable.

"""
x = "Banana ice-cream"
print(id(x))

""" 
FUNCTION PARAMETERS
Paramaters are the variables requested for a function, argument refers the value assigned to the function parameter

- Rule of thumb: make it that your fuction has more than 5 parameters, you should rewrite your code in a way that it takes fewer arguments.

"""
#example:

def times_3_mod_7(n):
  return(n*3)%7


print(times_3_mod_7(12)) # 12 is the argument

""" 
VARIABLE SCOPE
A variable can only be accessed from within the function, if not, you get an error

However, if a variable has been associated to a value prior to its use inside a function, then the variable will still be associated with the value outside the function. Try changing the variable name from the code bellow from x to w.

Where does the variable live?
variables that are in a f(x) live inside the f(x). Functions live in the console, even if they are within a function. Only variables are destroyed at the end of a function

However, to make a variable save inside the environment,you use global
"""

def add_2(x):
    return x + 2

print(add_2(1))
print(x)

x = 2

def add_2_then_times_3():
    def add_2():
        return x + 2
    return 3*add_2()

print(add_2(x))

"""
Example for global:
"""
x = 2

def add_n(n):
    global x # telling the add_n function to look for `x` in the global scope
    x += n
    return x

print(add_n(2))
print(x)
x = 6
print(x)
"""
Warning: avoid writing function that need to reach into the global scope, unless you have a good reason to do so
"""






